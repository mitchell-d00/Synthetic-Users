# Synthetic Users

Blind packet testing, smoke tests, and synthetic users and testers.

**Mitchell D. McPhetridge**

This repository is a guide to my testing work. The runnable suites, fixtures,
release workflows, and evidence live with the projects that produced them.
It starts with B-Tests and Combined MPLPB, then maps related experiments and
automation across the portfolio.

- [Test method and operator workflow](docs/TEST_METHOD.md)
- [How I automate and test MPLPB, with runnable examples](docs/MPLPB_AUTOMATION.md)
- [Automation and project inventory](docs/AUTOMATION.md)

## The kinds of tests

| Test | What runs | What to check |
|---|---|---|
| **Scripted synthetic user** | An executable case builds a workspace, supplies a task, and checks the result. | Decisions, citations, budgets, state changes, and negative controls against predeclared expectations. |
| **Blind packet test** | A fresh tester receives an assigned packet. The evaluator keeps the scoring key and other conditions separate. | Whether the tester finds original evidence, applies the current rule, reports uncertainty, and carries the right state forward. |
| **Smoke test** | A small path runs against an actual CLI, archive, installed package, browser, or deployment. | Whether the named path starts and completes in the tested environment. |
| **Regression or contract test** | A pinned suite exercises known positive and negative cases. | Whether the tested behavior holds for that version and fixture set. |
| **Native effect check** | An authorized case and prohibited cases reach the system's own decision or execution boundary. | Whether the expected effect actually happened, using a separate readback from the system's explanatory text. |

A scripted user is a fixture with a role and a task. A fresh model session can
serve as a synthetic tester, and an operator can run the same packet by hand.
Record which kind ran. Dependent handoff sessions form one chain and should be
reported with that dependency visible. [B-Tests protocol][protocol]

## Recorded examples

| Run | Recorded result |
|---|---|
| [Five mixed-dump users][mixed] | Five separate ledgers. The maps account for 19 processed files, 60 extracted statements, and 11 review links. All five strict decisions held at both exploration budgets. |
| [Randomized d100 batch][d100] | Five sets of five scripted users, four topics each, 25 ledgers, and 100 cases. All cases matched their scripted outcomes, including 25 strict supported answers. The run retains 100 source maps and 100 workspace results. |
| [Fresh-session B-Tests][fresh] | Thirty actual target sessions across five instruction-level conditions. The testbench retains source-linked inputs, outputs, failure cases, and transfers. Those runs measure the behavior of the supplied prompting treatments. |
| [Native Combined MPLPB rerun][native] | At `bbf6690`, 1,267 native tests, seven additional checks, 52 public controls, and seven work-boundary probes passed. The installed-wheel workspace check also passed. The 22-question historical replay retained two complete answers. |

The d100 seed randomizes topics, roles, actors, case order, profiles, file
formats, layouts, and exploration budgets. The public catalog supplies topic
names and URLs, while fictional records supply the cases’ evidence. The same
seed recreates the inputs, and a fresh seed changes the selection. The published
keys make these development runs replayable. Use an evaluator-held key with a
new batch for a fresh test. A historical-accuracy claim needs independently
selected originals and human scoring. [Frozen d100 run and paper][paper]

## Run the mixed-dump tests

Clone B-Tests and Combined MPLPB side by side. The example pins the B-Tests
release with the documented harness and the exact target used for the
recorded run.

```sh
git clone https://github.com/mitchell-d00/B-Tests.git
git clone https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages.git combined
git -C B-Tests checkout --detach d3abacedd57a324cbfa366a9592461420480d55c
git -C combined checkout --detach bbf6690d69b32d16969cc10e5ce9d380427ead40
cd B-Tests
python -m unittest discover -s tests -q
python -m research_lab.sorter_mixed_users --mplpb-root ../combined --out /tmp/mplpb-mixed-users
python -m research_lab.sorter_random_batches prepare --out /tmp/mplpb-d100-batch
python -m research_lab.sorter_random_batches run --mplpb-root ../combined --out /tmp/mplpb-d100-batch
```

Use a fresh output directory for each run. Add `--seed 502548331403503517`
to `prepare` to recreate the published d100 packets. The runner freezes the
target revision, the catalog and code hashes, and the input files. Keep
`operator-key.json` outside the target session. The native MPLPB run can inspect
both processed and approved material as declared by the fixture. [Full run record][native]

[protocol]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/PROTOCOL.md
[mixed]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/evaluation/mplpb-updates/bbf6690d69b32d16969cc10e5ce9d380427ead40/mixed/summary.json
[d100]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/evaluation/mplpb-updates/bbf6690d69b32d16969cc10e5ce9d380427ead40/d100/summary.json
[fresh]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/README.md#what-the-testbench-has-tested
[native]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/evaluation/mplpb-updates/bbf6690d69b32d16969cc10e5ce9d380427ead40/RESULTS.md
[paper]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/docs/paper/MPLPB_MIXED_DUMP.md
