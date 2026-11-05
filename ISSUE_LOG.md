# R Theory repository issue log

**Last reviewed:** 2026-11-04  
**Scope:** Documentation, infrastructure, provenance, and research-status discrepancies observed during the repository review.  
**Policy:** This log records follow-up work; it does not silently change mathematical claims or upgrade their evidence status.

## Documentation

### DOC-001 — Root README is out of date
- **Status:** Open
- **Priority:** High
- **Finding:** The root README describes Books 0–22 and Volumes 0–IV, omitting Books 23–24 and Volume V.
- **Action:** Refresh the series map, navigation links, status discipline, and coverage caveats. (Addressed in this documentation branch.)

### DOC-002 — Validation README coverage boundary
- **Status:** Open
- **Priority:** High
- **Finding:** The validation inventory documents detailed scripts for Books 0–19 and the Volume IV overview, but does not provide equivalent coverage documentation for Books 20–24.
- **Action:** State the boundary explicitly and add a per-book coverage matrix before implying uniform validation. (Addressed in this documentation branch.)

### DOC-003 — Scanner automation state is unverified
- **Status:** Open
- **Priority:** High
- **Finding:** Scanner documentation describes a daily cron and automatic pushes. The pointer records `{"next":10}`; the inspected scan log ends 2026-10-26.
- **Action:** Verify scheduler configuration and recent execution history. Reconcile the scheduler, pointer, and log. Do not infer active/inactive status from the log alone. (README clarified in this documentation branch.)

### DOC-004 — Research index and calibration need reconciliation
- **Status:** Open
- **Priority:** High
- **Finding:** The research index/calibration material appears to lag later Appendix P and Volume V developments, including differing descriptions of the B-7 twist lemma/proof status.
- **Action:** Reconcile each summary statement against the current derivations, Appendix P, and open-gate records; preserve conditional and incomplete status where applicable.

### DOC-005 — Manuscript README understates rewrite scope
- **Status:** Open
- **Priority:** Medium
- **Finding:** The README describes the rewrite as Books 0–22 and Volumes 0–IV, while the current series extends through Books 23–24 and Volume V.
- **Action:** Clarify the rewrite scope and distinguish it from the smaller set of original manuscript snapshots available in this directory. (Addressed in this documentation branch.)

### DOC-006 — Backup mirror synchronization claims need dated evidence
- **Status:** Open
- **Priority:** Medium
- **Finding:** The selected backup mirror README has already been revised to describe its limited scope and avoid claiming byte-level parity without a comparison. Its historical sync statement should remain clearly historical.
- **Action:** For each future sync, record source and mirror commit SHAs, included/excluded paths, comparison method, and date. No new mirror sync is claimed by this log.

## Infrastructure and provenance

### INF-001 — Database snapshot counts need reproducible provenance
- **Status:** Open
- **Priority:** Medium
- **Finding:** Database documentation reports 1,141 theorem records, 199 dependency edges, and 283 terms. These counts have not been independently confirmed by a fresh parse during this review.
- **Action:** Recompute from the checked-in database snapshot and record the query/script, snapshot hash, and result.

### INF-002 — Referenced artifacts are missing from the inspected tree
- **Status:** Open
- **Priority:** Medium
- **Finding:** Research calibration references `vol4/physics_interface/WITNESS_CANDIDATES.md`, and Book 23 references an import-contract draft; neither artifact was found in the inspected repository tree.
- **Action:** Confirm whether these files were renamed, moved, intentionally omitted, or need to be restored. Update references accordingly.

## Research status and evidence boundaries

### RES-001 — Book 23 sector occupancy remains asserted
- **Status:** Open
- **Priority:** High
- **Finding:** Book 23 sector occupancy is explicitly an ASSERTED empirical input, not a derived result. The receiving block/bridge equations remain open.
- **Action:** Keep the assertion label visible and identify the exact derivation or evidence required to close the bridge.

### RES-002 — Book 24 physical bridges remain open
- **Status:** Open
- **Priority:** High
- **Finding:** Conditional IO-word algebra results are present, but the physical `Oprop`, `E_k` contact operators, physical C8 action, and physical ten-plane/measurement bridge remain open.
- **Action:** Keep algebraic results distinct from physical realization; document the assumptions and evidence needed for each bridge.

## Audit interpretation

The Volume IV audit summary reports 407 assertions, 18 incorrect-as-stated findings, and `Δ_op(Volume IV)=∅`. A zero-failure run of the audit script means the script completed its checks; it does **not** mean there are zero manuscript errors.

## Change history

- 2026-11-04 — Initial issue log and documentation refresh prepared on branch `docs/2026-11-04-readme-and-issue-log`.
