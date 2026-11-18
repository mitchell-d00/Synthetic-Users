# How I automate and test MPLPB

**Mitchell D. McPhetridge**

I start with a named commit, a fixture that can fail, and a place to keep the
evidence. I want to be able to reopen the exact source, rerun a decision, and
see the effect independently. The following commands use the same tools as
the Combined repository. Where I show a shorter workflow, it is a reusable
example for that part of the job.

## How the pieces fit

| Stage | What I run | What I keep |
|---|---|---|
| Handoff | Build and verify the handoff manifest when the candidate changes. | Revision, update record, and source inventory. |
| Native regression | Run the Python suite plus UI, JavaScript, transport, and crawler checks. | Commands, exit status, logs, and frozen fixture results. |
| Archive first | Package the exact submitted Git tree, record the ZIP hash, extract it cleanly, and run the input fixtures against the extracted copy. | Commit, tree, archive hash, and a per-command report. |
| Installed wheel | Build the wheel from the extracted source and run its workspace smoke in isolated Python. | Wheel digest and a report showing which installed package supplied the feature. |
| Browser candidate | Build with the pinned WebAssembly runtime and run real Chromium against the candidate. | Browser and runtime identity, checked paths, and smoke results. |
| Public deployment | Publish on the approved branch, then smoke-test the deployed site. | A separate receipt for the public URL and published revision. |
| Synthetic and blind testing | Build separate ledgers for scripted users. Give a fresh model or manual tester only its assigned packet in a blind run. | Seeds, fixture and packet hashes, exact source spans, native decisions, untouched submissions, and scorer outputs. |

[Archive-first workflow][zip] · [Deployment workflow][pages] · [Committed handoff][handoff] · [Combined test index][index]

## Run the archive checks locally

Use a clean Combined checkout at the commit you mean to test. The
[example shell runner](../examples/mplpb-verify.sh) captures the selected Git
commit and tree and delegates to Combined's own frozen-source runner. Its
output contains the archive, the extracted source, `report.json`, and numbered
check logs. It returns the test runner's exit status and retains the reports
when a check reports failure.

```sh
# Run from this Synthetic-Users checkout. ../combined is a separate checkout.
mkdir -p /tmp/mplpb-evidence
bash examples/mplpb-verify.sh ../combined /tmp/mplpb-evidence/boundary boundary

# Use a different directory for the full run.
bash examples/mplpb-verify.sh ../combined /tmp/mplpb-evidence/full full
```

The full mode runs from the ZIP and includes the public evidence controls.
Use a Linux or macOS environment with Python 3.12 and Git. The helper uses
`sha256sum`, which ships on Linux and is available through GNU coreutils on
macOS. The full suite needs localhost sockets for HTTP fixtures.
The upstream [reproduction runner][reproduce] defines the exact checks.

For a quick checkout check, I run the targeted suite first so I can locate
a boundary failure before running the longer set:

```sh
cd ../combined
python -m unittest tests.test_candidate_workspace tests.test_witness_admission tests.test_sorter -q
python tools/check_ui_script.py
node tools/check_browser_transport.cjs
node tests/javascript-api.cjs
node crawler/test_worker.mjs
```

Practical example. The candidate workspace previously failed after wheel
installation because a byte-mapping import depended on checkout-only tooling.
I moved that projection into the installed runtime and added a clean-wheel
check to the archive workflow. The wheel's isolated interpreter exercises
an actual candidate replay, confirms the original still supports the strict
answer, and checks that the processed copy receives no approval.
[Installed smoke code][wheel] · [Recorded candidate workspace results][report]

### Rerun the wheel and deployed smoke separately

From the successfully extracted archive directory, build and exercise the
wheel in a fresh environment. The smoke writes JSON evidence and uses
isolated Python so the repository checkout cannot supply a missing package.

```sh
cd /tmp/mplpb-evidence/boundary/source
WHEEL_RUN=$(mktemp -d)
python -m pip wheel . --no-deps --wheel-dir "$WHEEL_RUN/wheels"
python -m venv "$WHEEL_RUN/venv"
"$WHEEL_RUN/venv/bin/python" -m pip install --no-index "$WHEEL_RUN"/wheels/*.whl
"$WHEEL_RUN/venv/bin/python" -I tools/check_candidate_workspace_install.py \
  --output "$WHEEL_RUN/workspace-smoke.json"
(cd "$WHEEL_RUN/wheels" && sha256sum ./*.whl > SHA256SUMS)
```

After the Pages workflow publishes your release, run the deployed-only smoke
against its URL. The upstream CI installs Playwright and a Chromium-compatible
browser before this step. A built preview can be checked separately with
`--preview-dir dist`. [Browser smoke runner][browser] · [Pages workflow][pages]

```sh
python tools/browser_release_smoke.py --live-url "$PUBLISHED_URL" --live-updated
```

## Walk an allowed case and a stopped case

The [native example](../examples/candidate_boundary.py) creates a fresh
fictional ledger and an exact processed copy. It verifies a strict answer
from the designated original, checks the candidate's actual byte span and
budget charge, withdraws the original, and reruns the same question.
The old workspace must refuse replay. The processed text should still be
inspectable with zero eligible owners.

```sh
# Run from Synthetic-Users with the pinned Combined source alongside it.
PYTHONPATH="$(cd ../combined && pwd)" python3 examples/candidate_boundary.py
```

This pattern keeps the positive and the condition that should stop it in the
same test. The [native B-Tests probes][native] extend it to actual effects.
They retain the artifact or state readback alongside the execution decision.

## Put the ZIP check in a GitHub workflow

This small example belongs in a Combined checkout or a compatible fork that
contains `tools/reproduce_boundaries.py`. Save it as
`.github/workflows/check-source-archive.yml`. The full Combined workflow adds
wheel, JavaScript, MCP, WebAssembly, and browser checks. Publishing happens in
the separate Pages workflow. [Complete release workflow][zip]

```yaml
name: Check exact source archive

on:
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  source-boundaries:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha || github.sha }}
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Test the extracted commit archive
        shell: bash
        run: |
          set -euo pipefail
          revision=$(git rev-parse HEAD)
          python -m tools.reproduce_boundaries \
            --revision "$revision" --suite boundary \
            --output "$RUNNER_TEMP/mplpb-source-check"
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: mplpb-source-boundaries
          path: |
            ${{ runner.temp }}/mplpb-source-check/report.json
            ${{ runner.temp }}/mplpb-source-check/check-*.log
          if-no-files-found: warn
```

## Where I use the older work

- **Local Mirror and Smart Local MPLPB** put validation and bounded routing on
  small local page collections. The same questions carry into the release
  tests about eligible ownership, ambiguity, and refusal. [Local Mirror][mirror] · [Smart Local][smart]
- **Networked and Swarm MPLPB** supply component checks for federation,
  provenance depth, profiles, and concurrent actors. I keep component evidence
  attributable to the bundled implementation and its own fixtures. [Networked][network] · [Swarm][swarm] · [Bundled-component results][parts]
- **Portable Evidence Runtime** exercises a transferable evidence capsule in
  native Python, JavaScript, and an offline browser. It demonstrates why I
  exercise a packaged artifact as a user receives it. [Portable runtime tests][portable]
- **MPLPB Residual Experiment** records the corpus and cases before reading
  them, then compares lookup, version-aware history, and enforceable
  eligibility in fresh processes. The input trace and refusal controls carry
  through to my current recovery tests. [Residual experiment][residual]
- **Advanced MPLPB** adds individual and all-project API smoke paths with
  versioned bundled assets and an evidence checklist. [Project API hub][advanced]
- **B-Tests** runs the five mixed-dump users and the seeded d100 batch. I
  retain one source map per case and keep the expected outcomes outside
  the target packet. Start with the [rerun commands and retained results][btests].
  For a held-out study, keep the evaluation key with a separate operator and
  have independent reviewers score exact citations and justified outcomes.
  [Blind handoff method][blind]

[zip]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/.github/workflows/zip-release-validation.yml
[pages]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/.github/workflows/pages.yml
[handoff]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/.github/workflows/handoff.yml
[index]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/docs/RESULTS_AND_TESTS.md
[reproduce]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/tools/reproduce_boundaries.py
[wheel]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/tools/check_candidate_workspace_install.py
[report]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/evaluation/candidate-review-workspace/2026-11-18-runtime/REPORT.md
[native]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/docs/MPLPB_NATIVE_COMPARISON.md
[mirror]: https://github.com/mitchell-d00/-The-Local-Mirror-MPLPB-as-a-Self-Contained-Offline-Site
[smart]: https://github.com/mitchell-d00/SMART-LOCAL-MPLPB-A-Retrieval-Bounded-Front-End-for-a-Local-Web
[network]: https://github.com/mitchell-d00/networked-mplpb
[swarm]: https://github.com/mitchell-d00/mplpb-swarm-scale
[parts]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/docs/MPLPB_NATIVE_COMPARISON.md#full-suite-and-component-checks
[portable]: https://github.com/mitchell-d00/portable-evidence-runtime
[residual]: https://github.com/mitchell-d00/mplpb-residual-experiment
[advanced]: https://github.com/mitchell-d00/Advanced-MPLPB-Provenance-Gated-Refusal-Ledger
[btests]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/evaluation/mplpb-updates/bbf6690d69b32d16969cc10e5ce9d380427ead40/RESULTS.md
[blind]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/docs/BLIND_HANDOFF_EXPERIMENT.md
[browser]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/tools/browser_release_smoke.py
