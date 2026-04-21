# stme_demo.py
# Demo v1 for STME (CLI version)
# Purpose:
# 1. Show how a traditional system collapses into one answer
# 2. Show how STME preserves multiple active states
# 3. Show how states can be reused across cycles

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
        next_states.append(
            State(
                name=state.name,
                score=updated_scores.get(state.name, state.score),
                risk=state.risk,
                status=updated_status.get(state.name, state.status),
                notes=updated_notes.get(state.name, state.notes),
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

    print_divider("STME DEMO — STATE-BASED DECISION SPACE ENGINE")
    print("A system that evaluates without collapsing decision space.")
    print("This demo compares a traditional single-answer flow with STME.\n")

    print_traditional_output(question, traditional_answer)
    print_stme_output(question, states)
    print_state_persistence()

    next_cycle_states = simulate_next_cycle(states)
    print_next_cycle(next_cycle_states)

    print_divider("FINAL NOTE")
    print("STME does not choose for you.")
    print("It keeps your choices alive.")


if __name__ == "__main__":
    main()