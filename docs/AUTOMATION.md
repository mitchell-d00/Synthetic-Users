# Automation and project inventory

The source links identify where checks are implemented. For an observed pass
or failure, use the linked result, release report, or exact GitHub Actions run.

## B-Tests

| Surface | Automation and evidence |
|---|---|
| [Offline harness and replay][b-ci] | GitHub Actions runs unit and negative controls, replays retained model results, and records unavailable native checks explicitly. Replay rechecks recorded evidence and scoring without issuing new model requests. |
| [Blind preparation and submission][b-blind] | The harness prepares assigned packets, records allowed sources and scoring metadata, and accepts the original response and receipt. The operator controls which files and conditions a target receives. |
| [Synthetic users and mixed inputs][b-results] | The native runners create separate ledgers, preserve source hashes, build and replay candidate workspaces, and retain source maps and expected versus observed outcomes. Seeded d100 rolls make each random assignment replayable. |
| [Pinned native suites and boundary probes][b-native] | Version checks, process exit statuses, command logs, positive effects, and independent event or artifact readbacks accompany the results. Historical comparisons keep the old and new revisions distinct. |

## Combined MPLPB

[Hands-on commands, release workflow example, and native demo](MPLPB_AUTOMATION.md)

| Surface | Automation and evidence |
|---|---|
| [Regression workflow][m-pr] | Runs the native Python suite, replay of frozen reference evidence, synthetic researcher journeys, crawler and transport tests, and JavaScript API checks. Browser jobs exercise the compiled runtime and researcher workflows. |
| [Archive-first release validation][m-zip] | Freezes the exact candidate tree into a ZIP, extracts and tests that content, checks the clean installed wheel, and exercises browser and WebAssembly paths. Retains the source pin, archive hash, and gate report. |
| [Public Pages build and smoke][m-pages] | Builds and publishes the browser runtime and runs a separate smoke against the newly published site. The build, deployed smoke, and candidate ZIP checks each have their own recorded outcome. |
| [Study worker isolation][m-study] | Verifies the controlled study worker, including runtime separation and evidence handling. Isolation receipts describe the observed software environment. |
| [Handoff workflow][m-handoff] | Builds and checks the committed handoff, update record, and source inventory. It keeps the revision and coordination state traceable for the next worker. |
| [Result index and synthetic suites][m-results] | Links relation-graph synthetic users, fictional researcher journeys, user collection and policy fixtures, procedure recovery, conversation cases, response-edge smoke tests, browser helpers, and the tests and reports associated with each family. |

For example, the PR #52 [archive-first run][m-zip-run] and the [postmerge
deployment smoke][m-pages-run] give distinct GitHub receipts. The [B-Tests
PR52 report][b-results] contains a separately executed native replay and the
mixed-dump and d100 evidence.

## Related repositories

| Project | Testing work |
|---|---|
| [Portable Evidence Runtime][per] | Offline synthetic scenarios, Python and JavaScript verification, and browser checks for a portable evidence capsule and separate authoring workspace. |
| [MPLPB Residual Experiment][residual] | A repeatable multi-arm pilot over recovery, retired sources, competing owners, integrity, and refusal. Uses a pinned Combined checkout and its own verifier. |
| [Advanced MPLPB][advanced] | Browser-local project API hub with individual and all-project smoke checks, versioned project snapshots, asset verification, and release evidence links. Includes checks for the calculator and pendulum projects it bundles. |
| [OwnerGate][gate] | Native gateway, disposable HTTP demonstration, and browser checks for policies, scope, and observed access decisions. |
| [Virtual DMV and Bot Traffic][dmv] | Fictional machine participation policy scenarios with a local registry, Python tests, browser probes, signed fixtures, and recorded red-to-green bug cases. |
| [Boundary Test Protocol][boundary] | Copy-paste chatbot test prompts, worked scoring examples, and a manual log for a fixed set of behavior checks. The rubric is available for reuse. |
| [Scope-Scan][scan] and [Scope Run Time][scope] | Scanner and constraint-pruning suites with pinned or declared examples and repeatable commands. |
| [Local Mirror][mirror], [Smart Local][smart], [Networked MPLPB][network], [Swarm MPLPB][swarm], and [MPLPB Image][image] | Component checks for local page validation, bounded routing, federation, concurrent use, and provenance for image artifacts. The bundled versions and fresh execution counts are identified in the [component evidence][parts]. |

[b-ci]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/.github/workflows/tests.yml
[b-blind]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/research_lab/blind_handoff.py
[b-native]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/docs/MPLPB_NATIVE_COMPARISON.md
[b-results]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/evaluation/mplpb-updates/bbf6690d69b32d16969cc10e5ce9d380427ead40/RESULTS.md
[m-pr]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/.github/workflows/pr-validation.yml
[m-zip]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/.github/workflows/zip-release-validation.yml
[m-pages]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/.github/workflows/pages.yml
[m-study]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/.github/workflows/study-sandbox.yml
[m-handoff]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/.github/workflows/handoff.yml
[m-results]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/docs/RESULTS_AND_TESTS.md
[m-zip-run]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/actions/runs/44342897295
[m-pages-run]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/actions/runs/44346501284
[per]: https://github.com/mitchell-d00/portable-evidence-runtime
[residual]: https://github.com/mitchell-d00/mplpb-residual-experiment
[advanced]: https://github.com/mitchell-d00/Advanced-MPLPB-Provenance-Gated-Refusal-Ledger
[gate]: https://github.com/mitchell-d00/OwnerGate
[dmv]: https://github.com/mitchell-d00/Virtual-DMV-Bot-Traffic-Research-Rig
[boundary]: https://github.com/mitchell-d00/Boundary-Test-Protocol-
[scan]: https://github.com/mitchell-d00/Scope-Scan
[scope]: https://github.com/mitchell-d00/Scope-Run-Time
[mirror]: https://github.com/mitchell-d00/-The-Local-Mirror-MPLPB-as-a-Self-Contained-Offline-Site
[smart]: https://github.com/mitchell-d00/SMART-LOCAL-MPLPB-A-Retrieval-Bounded-Front-End-for-a-Local-Web
[network]: https://github.com/mitchell-d00/networked-mplpb
[swarm]: https://github.com/mitchell-d00/mplpb-swarm-scale
[image]: https://github.com/mitchell-d00/MPLPB-Image-A-Signed-Retrieval-Bounded-Wall-for-Generated-and-Captured-Pictures
[parts]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/docs/MPLPB_NATIVE_COMPARISON.md#full-suite-and-component-checks
