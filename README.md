# R Theory — A Visual Rewrite

A book-by-book, intuition-first rewrite and research companion for the *R Theory* manuscript. The current series covers **Books 0–24** across **Volumes I–V**, with **Volume 0** maintained as a separate witness track rather than a chronological continuation.

The rewrite leads with visual intuition and interactive graphs, then records formal derivations, audit results, and the status of unresolved claims. Status labels are intentionally conservative: a numerical check, a symbolic check, an imported theorem, and a proof are not interchangeable.

## Read the series

- **Live site:** <https://cosbykit-afk.github.io/r-theory-rewrite/>
- [Series contents](contents/) — book and section navigation
- [Series index](index/) — searchable subject index
- [Appendix proofs](appendix-proofs/) — proof and derivation materials
- [Research companion](research/) — current research notes and open questions
- [Issue log](ISSUE_LOG.md) — documentation, infrastructure, and research follow-ups

Live Desmos calculators require an internet connection. Where provided, static PNG fallbacks are available when the interactive graphs cannot load.

## Series structure

| Track | Books | Scope |
|---|---:|---|
| Volume I | 0–6 | Foundational rewrite |
| Volume II | 7–13 | Extended development |
| Volume III | 14–16 | Further mathematical development |
| Volume IV | 17–19 | The Discrete Octant and the Computational Frontier |
| Volume 0 | 20–22 | Exact Witnesses at the Physics Boundary; separate witness track |
| Volume V | 23–24 | Later research and conditional constructions |

Volume 0 is not presented as a chronological continuation of Volumes I–IV. Its witness material is not, by itself, evidence of a new physical law.

## Repository map

- `book0/`–`book24/` — book pages and supporting figures, where present
- `contents/`, `index/` — series navigation and index
- `appendix-proofs/`, `appendix/` — proof appendices and supporting material
- `research/` — research companion, calibration, and open-gate notes
- `validation/` — validation scripts and their documented coverage
- `manuscript/`, `pdf/` — read-only source snapshots and exports
- `scanner/` — scanner documentation, pointer, and historical scan log
- `database/` — database exports, schema, and related documentation
- `vol0/`, `vol4/`, `vol4-audit/`, `e8/`, `tables/`, `guide/` — supporting material

Consult the repository tree for the authoritative current file inventory; not every directory contains a complete book-by-book implementation.

## Evidence and status discipline

Claims must retain the status justified by their evidence. In particular:

- **PROVED** — a proof is supplied within the stated assumptions and scope.
- **CHECKED** — a defined symbolic, numerical, computational, or structural check passed; this is not automatically a proof.
- **ASSERTED** — stated or imported as a premise without a derivation in the cited material.
- **INCOMPLETE / OPEN** — required derivation, bridge, or evidence remains outstanding.
- **REFUTED / INCORRECT-AS-STATED** — a claim fails as written, or is valid only under narrower conditions.
- **IMPORTED** — relies on an external result; its source and applicability should be identified.

Do not promote an assertion, numerical check, conditional result, or imported theorem into a proof without the corresponding argument. Preserve source labels and distinguish editorial reconstruction from the original manuscript.

## Audit and coverage notes

- The Volume IV audit summary reports **407 assertions**, including **18 incorrect-as-stated findings**, and `Δ_op(Volume IV)=∅`. A zero-failure audit-script run does not mean the manuscript contains zero errors.
- Validation documentation describes detailed script coverage for Books 0–19 and the Volume IV overview. It does **not** establish equivalent script coverage for Books 20–24.
- Volume 0 is a separate witness track; its essays should not be represented as establishing new physical law.
- In Volume V, Book 23 sector occupancy is explicitly marked **ASSERTED**, not derived. Book 24 contains conditional IO-word algebra results, while the physical operator, contact-operator, physical C8-action, and ten-plane/measurement bridges remain open.
- Database documentation records a snapshot of 1,141 theorem records, 199 dependency edges, and 283 terms. These are documented snapshot counts, not independently certified here by a fresh database reparse.

For specific gaps and follow-up work, see [ISSUE_LOG.md](ISSUE_LOG.md).

## Source and license

This rewrite is a separate commentary and research layer. Original manuscript snapshots are retained as read-only references and are not modified by this project.

Public domain — [The Unlicense](LICENSE).
