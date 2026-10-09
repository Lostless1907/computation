# Knight-Independent N-Queens

Computational companion to a mathematical investigation of knight-independent
N-Queens placements and the graphs induced by knight moves between queens.

## Setup

    python -m venv .venv
    source .venv/bin/activate
    pip install -e '.[test]'
    make test
    make reproduce

Set `MAX_N=15` to reproduce the exhaustive enumeration through order 15.
This may require substantial runtime.

## Components

- Python: exhaustive enumeration, local statistics, randomized search.
- NetworkX: induced graphs, graph invariants and exact isomorphism tests.
- C: independent placement verifier.
- SageMath: finite checks of the modular construction.
- Lean 4: formalization of the knight-adjacency relation.
- LaTeX: `paper/computational_work.tex`, the computational-work section
  intended for inclusion in the research paper.

## Evidence policy

Exhaustive enumeration, randomized search, finite verification, and
mathematical proof are different kinds of evidence. A failed bounded search
does not prove nonexistence. Finite tests do not establish universal claims.
Known existence constructions must be credited to their published sources.

The scripts regenerate finite data. The manuscript's mathematical proofs
remain responsible for all general theorems.
