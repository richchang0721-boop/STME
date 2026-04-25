# stme_demov2.py
# Demo v2 for STME + Abstract Constraint Layer (NDF placeholder)
# Purpose:
# 1. Show how a traditional system collapses into one answer
# 2. Show how STME preserves multiple active states
# 3. Show how decision space evolves across cycles
# 4. Show how an external constraint layer (e.g., NDF) can influence
#    long-horizon state evolution without collapsing the decision space
# Note:
# This demo does not implement the full constraint mechanism.
# It only illustrates how decision-space outputs may be subject to
# external constraint layers in a larger architecture.

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class State:
    name: str
    score: float
    risk: str
    status: str
    notes: str = ""


def print_divider(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def print_traditional_output(question: str, answer: str) -> None:
    print_divider("TRADITIONAL SYSTEM")
    print(f"Scenario:\n{question}\n")
    print("Traditional Output:")
    print(f"→ {answer}")
    print("\nCharacteristics:")
    print("- Single-path result")
    print("- All alternatives discarded")
    print("- Future changes require full recomputation")


def print_stme_output(question: str, states: List[State]) -> None:
    print_divider("STME OUTPUT")
    print(f"Scenario:\n{question}\n")
    print("Candidate States:\n")

    for idx, state in enumerate(states, start=1):
        print(f"[State {chr(64 + idx)}] {state.name}")
        print(f"- Score: {state.score}")
        print(f"- Risk: {state.risk}")
        print(f"- Status: {state.status}")
        if state.notes:
            print(f"- Notes: {state.notes}")
        print()

    print("Result:")
    print("- Multiple states preserved")
    print("- No decision collapse performed at STME layer")
    print("- All viable paths remain available for future transition")


def print_state_persistence() -> None:
    print_divider("STATE PERSISTENCE")
    print("Cycle 1:")
    print("A / B / C")
    print("\nCycle 2:")
    print("B ↑")
    print("C ↓")
    print("A (still available)")
    print("\nCycle 3:")
    print("A becomes dominant")
    print("\nMeaning:")
    print("- Existing states are reused across evaluation cycles")
    print("- The system does not need to regenerate the entire decision space")
    print("- State transitions remain adaptive over time")


def ndf_guard(states: List[State]) -> List[State]:
    """
    NDF placeholder layer.
    This does NOT implement real NDF logic.
    Only demonstrates pre-execution constraint hook.
    """

    guarded_states = []

    for s in states:
        notes = s.notes

        if s.risk == "High":
            notes += " | NDF flag: high-risk requires constraint review"

        # 模擬「不讓單一路徑 dominance」
        if s.score > 18.5:
            notes += " | NDF flag: dominance check placeholder"

        guarded_states.append(
            State(
                name=s.name,
                score=s.score,
                risk=s.risk,
                status=s.status,
                notes=notes,
            )
        )

    return guarded_states

def simulate_next_cycle(states: List[State]) -> List[State]:
    """
    A simple mock next-cycle update.
    This is intentionally hand-crafted for demo clarity.
    """

    updated_scores: Dict[str, float] = {
        "Switch job immediately": 18.6,
        "Wait and observe": 16.9,
        "Stay in current job": 15.4,
    }

    updated_status: Dict[str, str] = {
        "Switch job immediately": "Promoted",
        "Wait and observe": "Active",
        "Stay in current job": "Deferred",
    }

    updated_notes: Dict[str, str] = {
        "Switch job immediately": "Reactivated under improved external conditions",
        "Wait and observe": "Still viable under medium uncertainty",
        "Stay in current job": "Lower relative value after condition change",
    }

    next_states: List[State] = []
    for state in states:
        base_note = updated_notes.get(state.name, state.notes)

        if state.notes and state.notes not in base_note:
            base_note += " | " + state.notes

        next_states.append(
            State(
                name=state.name,
                score=updated_scores.get(state.name, state.score),
                risk=state.risk,
                status=updated_status.get(state.name, state.status),
                notes=base_note,
            )
        )

    return sorted(next_states, key=lambda s: s.score, reverse=True)


def print_next_cycle(states: List[State]) -> None:
    print_divider("NEXT EVALUATION CYCLE")
    print("Updated Candidate States:\n")
    for idx, state in enumerate(states, start=1):
        print(f"[State {chr(64 + idx)}] {state.name}")
        print(f"- Score: {state.score}")
        print(f"- Risk: {state.risk}")
        print(f"- Status: {state.status}")
        if state.notes:
            print(f"- Notes: {state.notes}")
        print()

    print("Observation:")
    print("- A previously non-primary state can become dominant")
    print("- STME preserves decision space instead of destroying it")
    print("- Final selection, if any, belongs to an external decision layer")


def main() -> None:
    question = "Should I switch to a new job this year?"

    traditional_answer = "Stay in current job"

    states = [
        State(
            name="Switch job immediately",
            score=15.2,
            risk="High",
            status="Active",
            notes="High upside but lower controllability",
        ),
        State(
            name="Wait and observe",
            score=17.5,
            risk="Medium",
            status="Active",
            notes="Balanced path under uncertainty",
        ),
        State(
            name="Stay in current job",
            score=18.0,
            risk="Low",
            status="Active",
            notes="Highest short-term controllability",
        ),
    ]

    print_divider("STME DEMO v2 — WITH ABSTRACT CONSTRAINT LAYER")
    print("A system that evaluates without collapsing decision space.")
    print("This demo compares a traditional single-answer flow with STME.\n")

    print_traditional_output(question, traditional_answer)
    print_stme_output(question, states)
    print_state_persistence()

    print_divider("NEXT CYCLE — WITHOUT CONSTRAINT (BASELINE)")
    baseline_states = simulate_next_cycle(states)
    print_next_cycle(baseline_states)

    print_divider("NEXT CYCLE — WITH NDF CONSTRAINT (ABSTRACT)")
    guarded_states = ndf_guard(states)
    ndf_states = simulate_next_cycle(guarded_states)
    print_next_cycle(ndf_states)

    print("Note: Output is subject to external constraint layers (e.g., NDF).")
    print_divider("FINAL NOTE")
    print("STME does not choose for you.")
    print("It keeps your choices alive.")


if __name__ == "__main__":
    main()