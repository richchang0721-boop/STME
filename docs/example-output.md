# Example Output

This example demonstrates how STME represents a real-world decision problem.

---

## Input Question

> Should I change jobs this year?

---

## State Representation

The decision is decomposed into multiple concurrent states:

| State | Content | Role | Perspective | Dynamics | Validity |
|------|--------|------|------------|----------|----------|
| ψ1 | Current job conditions | Core | Internal | Static | Real |
| ψ2 | Personal job satisfaction | Core | Internal | Static | Potential |
| ψ3 | External job opportunities | Functional | External | Static | Potential |
| ψ4 | Risks of switching jobs | Functional | External | Static | Real |
| ψ5 | Financial and stability considerations | Functional | Structural | Static | Real |
| ψ6 | Career growth alignment | Core | Internal | Static | Potential |
| ψ7 | Transition readiness | Functional | Structural | Static | Potential |

---

## Structural Analysis

The system evaluates the overall decision structure:

- **Core grounding:** partially real, partially potential  
- **Driver balance:** primarily internal  
- **Dynamics:** static dominant  

### Interpretation

This indicates that:

- The decision is still in an evaluation phase  
- Internal factors (goals, satisfaction) dominate over external pressure  
- Action has not yet been triggered  

---

## Transition Evaluation

STME identifies possible transitions between states:

| Transition | From | Goal | Cost | Time | Controllability | Impact | Score |
|-----------|------|------|------|------|----------------|--------|-------|
| Evaluate alignment between satisfaction and career goals | ψ2 | potential → real | 0.2 | 0.2 | 0.9 | 0.8 | 8.000 |
| Assess market opportunities | ψ3 | potential → real | 0.3 | 0.4 | 0.7 | 0.5 | 2.917 |
| Analyze risk vs stability | ψ4 | real → decision-ready | 0.5 | 0.5 | 0.8 | 0.4 | 1.280 |
| Evaluate financial stability | ψ5 | real → actionable | 0.6 | 0.6 | 0.7 | 0.4 | 0.778 |

---

## Interpretation of Transitions

The highest-ranked transitions focus on:

- clarifying internal alignment  
- converting potential states into grounded understanding  

Lower-ranked transitions relate to:

- external validation  
- risk assessment  

---

## Key Observation

The system does not suggest:

- switching jobs  
- staying in the current role  

Instead, it reveals that:

- the decision space is not yet fully grounded  
- internal alignment remains unresolved  
- premature action would collapse the structure too early  

---

## Final Note

STME does not make the decision.

It preserves the decision space and identifies:

- what is already grounded  
- what remains uncertain  
- what can be explored before commitment  

---

## One-Line Summary

The system does not answer the question.

It shows why the answer should not be decided yet.
