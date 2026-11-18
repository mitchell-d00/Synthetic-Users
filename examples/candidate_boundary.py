"""A small native proof-and-candidate check using a fictional local record."""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from mplpb_combined.ledger import withdraw, write
from mplpb_work.candidate_workspace import build, verify_workspace
from mplpb_work.sorter import sort_directory


def check(condition, reason):
    if not condition:
        raise AssertionError(reason)


def main():
    with TemporaryDirectory() as directory:
        root = Path(directory)
        originals = root / "originals"
        processed = root / "processed"
        processed.mkdir()

        title = "Redwood memorandum"
        statement = "Mara wrote the Redwood memorandum."
        question = "Who wrote the Redwood memorandum?"
        source = write(originals, doc_id="DOC-101", title=title, scope=title,
                       origin="human", body=statement)
        copy = processed / "copy.txt"
        copy.write_text(statement, encoding="utf-8")

        graph = sort_directory(processed, mode="compare")
        review = build(graph, processed, originals, question=question)
        decision = review["mplpb_decision"]
        check(decision["status"] == "one_eligible_owner", "Expected the designated original")
        check(decision["strict_answer"]["answer_supported"], "Original body did not support the answer")
        exact = next(candidate for candidate in review["candidates"]
                     if candidate["kind"] == "exact_match")
        span = exact["processed"]["span"]
        quote = copy.read_bytes()[span["byte_start"]:span["byte_end"]]
        check(quote == statement.encode("utf-8"), "Processed span differs from the original bytes")
        check(not exact["approval_transferred"] and not exact["answer_supported"],
              "A candidate acquired authority")
        check(review["exploration_budget"]["strict_slots_consumed"] == 0,
              "Exploration spent a strict passage slot")
        verify_workspace(review, graph, processed, originals)

        withdraw(originals, source.id, note="Synthetic withdrawal control")
        try:
            verify_workspace(review, graph, processed, originals)
        except ValueError:
            pass
        else:
            raise AssertionError("Stale workspace replayed after withdrawal")

        fresh = build(graph, processed, originals, question=question)
        check(fresh["mplpb_decision"]["status"] == "no_eligible_owner",
              "Withdrawn original still counted as eligible")
        check(fresh["processed_passages"] and not fresh["mplpb_decision"]["strict_answer"],
              "Expected exploration to remain available without strict support")
        print(json.dumps({
            "original_support": "PASS",
            "exact_candidate_and_byte_span": "PASS",
            "candidate_approval_unchanged": "PASS",
            "stale_workspace_replay_rejected": "PASS",
            "processed_only_exploration_after_withdrawal": "PASS",
        }, indent=2))


if __name__ == "__main__":
    main()
