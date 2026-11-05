# R Theory — A Visual Rewrite

A book-by-book, intuition-first rewrite of the *R Theory* manuscript (Volumes
0–V, Books 0–24). Each book leads with pictures and intuition (live Desmos
graphs), then the formal audit with proof statuses preserved.

## Read it

Live site: <https://kitcosby.github.io/r-theory-rewrite/>

Start with the [series contents](contents/) (every book, every section) or
the [series index](index/) (A–Z). Or open `index.html` in a
browser.

The graphs are live [Desmos](https://www.desmos.com) calculators (internet
required); if Desmos fails to load, static PNG fallbacks in each book's
`graphs/` folder are shown instead.

## What's here

- `book0/`–`book6/` — Volume I (Books 0–6)
- `book7/`–`book13/` — Volume II (Books 7–13)
- `book14/`–`book16/` — Volume III (Books 14–16)
- `book17/`–`book19/` — Volume IV: The Discrete Octant and the Computational
  Frontier
- `book20/`–`book22/` — Volume 0: Exact Witnesses at the Physics Boundary
- `book23/`–`book24/` — Volume V: The Physics Interface (Book 23: Chirality
  Anchors — the C-1 Physics Interface; Book 24: The IO-Word Campaign)
- `contents/` — series-wide table of contents, every section an anchor link
- `index/` — series-wide keyword index
- `tables/` — downloadable pre-computed tables (E8 30380 weight table,
  R1/R2/R3a/R3b, and the matrix archive)
- `guide/` — *A Guide to Creative Reason (after Euclid)*
- `research/` — research companion notes
- `validation/` — the numbered audit scripts behind the pages
  (PROVED / CHECKED / ASSERTED / INCOMPLETE)
- `database/` — R Theory database snapshot (per-table SQL, reassemble
  script, SAD architecture diagrams)
- `manuscript/`, `pdf/` — source snapshots
- `vol0/`, `vol4/`, `vol4-audit/`, `vol5/`, `e8/`, `appendix/`, `title/` —
  supporting material
- `ISSUE_LOG.md` — dated, append-only log of documentation, infrastructure,
  and research findings against this repository, with closure criteria

## Status discipline

Book pages label claims with the scope the audit earned — checked proof,
completed symbolic check, completed numerical check, standard imported
theorem, manuscript assertion, assumption/axiom, or incorrect/incomplete.
Book 0 additionally preserves the original manuscript's own status tags
(CERTIFIED etc.), as disclosed on that page; those are the manuscript's
labels, not independent re-verification. Nothing is promoted beyond what the
mathematics supports.

## Audits

- **Volume I** (Books 0–6) — independent audit complete.
- **Volume II** (Books 7–13) — independent audit complete.
- **Volume III** (Books 14–16) — independent audit complete.
- **Volume IV** (Books 17–19) — audit in progress.

## Status (2026-11-04)

- Series index (A–Z) and full series contents with anchor links, covering
  Books 0–24.
- Live Desmos calculators in every book; static PNG fallbacks if Desmos
  fails to load.
- Theorem-status mirror: `sync_status.py` parses the audit ledger into
  `status_registry.json` (195 claims) and injects "Independent
  audit verdicts" tables into the book pages; inline status pills link to
  the canonical ledger. `derivations_registry.json` maps 86 audited claims
  and the Appendix P research results (P-1..P-6) to their derivations.
- R Theory database snapshot in `database/` refreshed 2026-11-04
  (1,141 theorems, 199 dependency edges, 283 terms).
- Site published via GitHub Pages; backup mirror in
  [R-Theory](https://github.com/kitcosby/R-Theory).

## Source

Rewrite of the *R Theory* manuscript (read-only original; this rewrite lives
here and does not modify it).

## License

Public domain — [The Unlicense](LICENSE).
