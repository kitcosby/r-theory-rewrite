# Issue Log — r-theory-rewrite

Dated, append-only. New findings are added as new entries; an entry's status
changes by appending a dated status line under it, never by rewriting the
original entry. Each entry carries: finding, classification, status,
evidence (file paths in this tree), and closure criteria. Research entries
(RES-*) record open questions at their audited scope — they are not bug
reports and close only as their criteria state.

---

## Opened 2026-11-04

### DOC-001 — Top-level README omits Books 23–24 and Volume V
- **Classification:** Documentation
- **Status:** Open (README revision proposed in the same change that opened
  this log; closes when that revision merges)
- **Evidence:** `README.md` described the series as "Volumes 0–IV, Books
  0–22" and its volume list stopped at `book22/`. The tree contains
  `book23/` ("Chirality Anchors — the C-1 Physics Interface"), `book24/`
  ("The IO-Word Campaign"), and `vol5/` ("Volume V — The Physics
  Interface"). The same README also pointed readers at the frozen legacy
  account's Pages site and mirror instead of this repository's Pages site
  and `kitcosby/R-Theory`.
- **Closure criteria:** Top-level README names Books 0–24 and Volumes 0–V,
  lists `book23/`–`book24/` and `vol5/`, and links the live Pages site and
  mirror on the `kitcosby` account.

### DOC-002 — Validation README documents Books 0–19, not Books 20–24
- **Classification:** Documentation / coverage
- **Status:** Open
- **Evidence:** `validation/README.md` scopes the published scripts to
  "`book0/`–`book19/` plus the Volume IV overview," and `validation/`
  contains per-book folders only through `book19/` (plus `vol4/`). The
  series now runs to Book 24; Books 20–24 have no validation folders and
  the README does not say so.
- **Closure criteria:** Either validation coverage extends to Books 20–24,
  or `validation/README.md` states plainly that Books 20–24 have no
  published validation scripts yet.

### DOC-003 — Scanner README describes a book0–book19 sweep; Books 20–24 sit outside it with no published note
- **Classification:** Infrastructure
- **Status:** Open
- **Evidence:** `scanner/README.md`: "One book per sweep, book0 -> book19,
  then wraps to book0." `scanner/pointer.json` (`{"next": 19}`) and
  `scanner/scan.log` (latest entries: book16 on 2026-11-02, book17 on
  2026-11-03, book18 on 2026-11-04) are consistent with that stated range.
  What no published note addresses: Books 20–24 exist in the tree but are
  outside the sweep's range, so they receive no daily polish pass.
- **Closure criteria:** A published decision, recorded in
  `scanner/README.md`: either the sweep range extends to cover Books
  20–24, or the exclusion is stated as deliberate with its reason.

### DOC-004 — Research index / calibration pages lag behind later Appendix P results
- **Classification:** Documentation consistency
- **Status:** Open
- **Evidence:** `research/calibration.html` ("Calibration Predictions")
  carries no date later than 2026-09-28 and no reference to Appendix P.
  `research/index.html` links "Appendix P — Full derivations," and
  `appendix-proofs/` holds the P-1..P-6 derivation set assembled after the
  calibration page's last update. The calibration predictions have not
  been reconciled against those later results in any published note.
- **Closure criteria:** `research/calibration.html` (or a linked research
  note) records, per prediction, whether the Appendix P results confirm,
  revise, or leave it unchanged — or states that the reconciliation was
  done and where its outcome lives.

### INF-001 — Database snapshot counts, registry figures, and coverage need a documented reconciliation
- **Classification:** Data / infrastructure
- **Status:** Open
- **Evidence:** The previous top-level README status section (dated
  2026-09-30) cited "`status_registry.json` (86 claims, Books 2–6)"; the
  86 figure is in fact the claims count of `derivations_registry.json`
  (86 claims, 39 results, generated 2026-09-28), while
  `status_registry.json` itself holds 195 claims (generated 2026-10-01).
  The `database/` snapshot was refreshed 2026-11-04 (1,141 theorems, 199
  dependency edges, 283 terms). No single published note reconciles these
  three figures or states what each registry covers.
- **Closure criteria:** A short published note (README or a `database/`
  companion) states each registry's coverage and generation date and the
  snapshot's counts and date, consistent with the files themselves.

### INF-002 — Book 23 and calibration pages refer to supporting contract/candidate files not present in the public tree
- **Classification:** Missing artifacts
- **Status:** Open
- **Evidence:** `book23/index.html` names
  `vol4/physics_interface/IMPORT_CONTRACTS_DRAFT.md`;
  `research/calibration.html` names
  `vol4/physics_interface/WITNESS_CANDIDATES.md`. Neither path exists in
  this repository (the public tree has no `vol4/physics_interface/`
  directory), so a reader cannot follow either reference.
- **Closure criteria:** Each named file is either published in the tree at
  the referenced path (or the reference updated to its published
  location), or the reference is annotated as an unpublished working file.

### RES-001 — Book 23's sector-occupancy input remains asserted, not derived
- **Classification:** Research
- **Status:** Open
- **Evidence:** `book23/index.html` uses sector occupancy as its
  orientation anchor and labels that input ASSERTED on the page itself
  (status pills: "ASSERTED — taken as input, not derived").
- **Closure criteria:** The sector-occupancy input is derived from the
  core operators and the page's labels updated to the earned scope, or
  the input is dropped by Kit Cosby's ruling and the page revised
  accordingly. (Stepping-stone rule: an asserted input is discharged by
  derivation or dropped — it does not close by relabeling.)
- **Status note (2026-11-05):** Review of `book0/index.html` §15 and the
  original Volume I manuscript confirms that Theorem 0.III.T1 is scoped to
  revised M0–M4 and the admitted T0–T3 orientation transformations. It
  concludes that this candidate universe represents orientation but does
  not derive a preferred physical chirality. Corollary 0.III.C2 explicitly
  allows a later physics-interface interaction, observable, source,
  boundary condition, or preparation law to distinguish the alternatives.
  Accordingly, "derived from the core operators" is a viable closure route
  only if it identifies a declared extension or physical input outside that
  theorem's candidate universe; a derivation from M0–M4/T0–T3 alone is not
  available under the theorem as stated. Book 23 §3 and
  `book23/CHIRAL-ANCHOR-02.json` continue to classify occupancy as
  ASSERTED-by-Kit. The Zeeman readout in Book 23 §2 establishes a
  field-sensitive polarization observable, but no published C-1 receiving
  block or bridge maps its sign to
  `sign(Re(z) * Im(z))`. The referenced
  `vol4/physics_interface/IMPORT_CONTRACTS_DRAFT.md` remains absent
  (also INF-002). RES-001 remains Open; no status promotion is made.

### RES-002 — Book 24's physical operator/matrix identifications and measurement bridge remain open
- **Classification:** Research
- **Status:** Open
- **Evidence:** `book24/index.html`, in its own words: "the dial
  identification via the D8/DW/DB ratios is the unidentified path"; the
  archived m0 = 2, m2 = 5 values "are reference values — a placeholder,
  not a physical selection"; standing conditions record that "g is not
  the physical C8 action, which stays open." No established operator in
  the page's record selects the physical identification, and the
  measurement bridge is stated as a requirement bound on a missing
  contact operator, not a derivation.
- **Closure criteria:** The physical operator/matrix identification and
  the measurement bridge are derived and the page's labels updated to the
  earned scope, or the items are closed by Kit Cosby's ruling as dropped
  or as proved no-go results at a stated scope.

### RES-003 — Book 24 two-needle dial equality and blind set
- **Classification:** exact algebraic consequence of Appendix P-3 T3/T4; independent exact computation; counterexample to the implication “gamma nonzero implies strictness.”
- **Status:** Open — equality/blind-set characterization derived and computationally supported; original T3/T4 block derivations and physical E_k/Oprop identifications were not re-audited.
- **Evidence:** Book 24 §2; Appendix P-3; focused audit in [BOOK24_TWO_NEEDLE_EQUALITY.md](research/BOOK24_TWO_NEEDLE_EQUALITY.md); GitHub issue [#61](https://github.com/kitcosby/r-theory-rewrite/issues/61).
- **Finding:** For the archived positive reference values m0=2, m2=5, DW*DB-D8^2 = 4C^2 + (29/5) C D8. Equality is equivalent to C=0, not gamma=0. If Z=U Sigma V^T is a thin SVD, C=||Sigma U^T gamma V Sigma||_F^2; the blind set is U^T gamma V=0. The exact nonzero-gamma witness is recorded in the research note.
- **Closure criteria:** preserve the conditional status of T3/T4; clarify the website exposition; independently review the original block derivations; identify the physical E_k/Oprop and dial-to-observable maps before any physical conclusion.

### RES-004 — Volume IV P_54 / 1820 / 135 representation chain
- **Classification:** representation/dependency clarification; partially resolved at the branching-content level.
- **Status:** Open — the 54-dimensional component is located in the 135 under the standard SO(10)×SU(4) branching; the explicit quadratic map and projector remain unconstructed.
- **Evidence:** Volume IV original manuscript, especially lines 742–750, 1669, and 1964–1970; Volume IV audit ledgers; Notion IC-19 and IC-20; GitHub issue [#47](https://github.com/kitcosby/r-theory-rewrite/issues/47) and cross-system issue [#53](https://github.com/kitcosby/r-theory-rewrite/issues/53).
- **Finding:** The physical 54 is a constituent of the 135, not a linear constituent of the 1820 under the standard embedding. The intended route is a quadratic map Sym^2(1820) -> 135 followed by a rank-54 projection inside 135. The current skeleton neither constructs this map nor applies P_54; its “54x54 or embedding in 1820” input is inconsistent with the stated route.
- **Closure criteria:** give the explicit equivariant quadratic map, basis/normalization, and rank-54 projector (or equivalent inclusion/projection pair); verify intertwining and idempotence; then recompute S_F. Keep the S_F/N_1820 numerical gate OPEN until then.


### RES-003 update — fixed-Z kernel bound (2026-11-06)
- **Classification:** exact conditional linear-algebra derivation.
- **Assumptions:** the candidate space \u1d53 is a 12-dimensional real linear subspace of the 368×556 gamma-matrix space, gamma ranges over that space, and Z is fixed with rank r.
- **Finding:** with thin SVD Z=UΣVᵀ, the compression map Φ_Z: b→M_r(R), γ↦UᵀγV has kernel equal to the two-needle blind set. Rank-nullity gives dim ker Φ_Z ≥ max(0,12−r²). Thus every fixed Z of rank 1, 2, or 3 has a nonzero b-blind element, with lower bounds 11, 8, and 3. For r≥4, dimension counting alone does not decide injectivity.
- **Limit:** this does not establish the physical rank of Z or that b is the final physical Oprop space. The actual b basis and fixed physical Z are still required for an exact rank test. No queue job was submitted because this is a direct rank-nullity proof.
