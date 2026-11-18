# Test method

## Prepare the same task for each target

1. Define the claim under test and the smallest observation that could
   distinguish a pass from a failure. For source support, specify the eligible
   original and the required quote or refusal. For enforcement, specify a
   state change or observable effect.
2. Freeze the revision, fixture bytes, expected outputs, source and profile
   rules, and budgets before execution. For a model run, also record the
   model, tools, instructions, and any operator assistance.
3. Include an authorized positive and a meaningful negative. Useful negatives
   include an absent source, two competing originals, an unapproved copy,
   a partial correction, changed bytes, and a revoked permission.
4. Give each arm the same underlying problem. Record difference in interfaces
   and preserve native output alongside any common scoring fields.
5. Keep target results, scoring, and readbacks separately attributable.
   Report the denominator, exact fixture and revision, and any incomplete
   condition. [B-Tests comparison design][protocol]

## How to run different kinds of testers

The native mixed-dump runner builds a fresh MPLPB ledger for each user. It
sorts the processed files, builds candidate workspaces, replays them, and
checks that exploration did not transfer approval or spend strict proof slots.
Each source map includes excluded files and extracted statements that did not
make the display. The randomized runner extends the same approach to balanced
scenario groups with seeded topic and user assignments. [Native mixed runner][mixed] · [Randomized runner][random]

For a fresh model session or manual tester, the evaluator prepares the
packet and shares only that target's entry instructions and permitted files.
Keep the key, other treatments, prior outputs, and repository result pages
out of the target session. Preserve the untouched response and transcript,
then score them outside the test session. Record actual access boundaries.
An instructional boundary on a shared filesystem is a weaker condition
than an enforced file-access boundary. A public development packet can be
replayed and should be treated as previously exposed material. [Blind handoff procedure][blind]

To compare strong governance prompting with an ordinary baseline, keep the
model, source corpus, task, tools, and budget constant where feasible, with
a fresh session for every treatment. Score the reported decision and citations.
If an interface exposes a real executor, test the actual system separately.
Read the resulting state through an independent surface. Follow the allowed
positive case as well as the prohibited case, so an adapter that never acts
cannot pass both. [Cross-system testbench guide][comparison]

For a native system other than MPLPB, add an adapter that invokes its normal
entry point and records its version, input hash, decision, citations, and
available readback. Keep unsupported extractions or unavailable effects
explicit in the result. [Native adapter boundary and paired probes][native]

## Interpret the evidence

- **PASS** means the named case met the recorded criterion. **FAIL** means
  the observed outcome violated that criterion.
- **NOT_RUN** records a missing execution or dependency. **INCONCLUSIVE**
  applies when the observations cannot decide the claim.
- A candidate link is evidence of discovery. A cited, eligible original is
  needed to check strict support. An independently read effect is needed
  to check enforcement.
- A browser smoke pass applies to the named browser, runtime and release.
  Record separately whether the source archive, candidate build, or public
  deployment was exercised.
- An independent historical evaluation requires new originals and questions
  selected outside development, concealed expectations, and independent review.
  Score complete answers against answerable cases. Score refusals, conflicts,
  and other correct outcomes against all cases. Log false links, omissions,
  citation fidelity, and human review effort separately. [Source study protocol][study]

[protocol]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/PROTOCOL.md
[blind]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/docs/BLIND_HANDOFF_EXPERIMENT.md
[mixed]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/research_lab/sorter_mixed_users.py
[random]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/research_lab/sorter_random_batches.py
[comparison]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/README.md#use-b-tests-with-another-system
[native]: https://github.com/mitchell-d00/B-Tests/blob/d3abacedd57a324cbfa366a9592461420480d55c/docs/MPLPB_NATIVE_COMPARISON.md
[study]: https://github.com/mitchell-d00/Combined-MPLPB-A-closed-local-ledger-of-pages-that-answers-only-from-those-pages/blob/bbf6690d69b32d16969cc10e5ce9d380427ead40/docs/ORIGINAL_RECORD_STUDY.md
