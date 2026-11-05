# R Theory repository issue log

Updated: 2026-11-04

This log records documentation, provenance, and research-status issues observed during the repository review. Entries distinguish confirmed repository/documentation gaps from research questions; they do not imply that every issue has been independently resolved.

## Documentation

### DOC-001 — Root README omitted Books 23–24 and Volume V
- **Status:** Addressed on this documentation branch.
- **Finding:** The previous README described Books 0–22 and Volumes 0–IV, although the repository now includes Books 23–24 and Volume V.
- **Action:** Refresh the series map, navigation links, evidence labels, and audit/coverage caveats.

### DOC-002 — Validation inventory stops at Books 0–19
- **Status:** Coverage boundary documented; later-book inventory remains open.
- **Finding:** validation/README.md documents Books 0–19 and the Volume IV overview, not equivalent coverage for Books 20–24.
- **Action:** State the documented boundary explicitly and build a later-book coverage matrix when authoritative scripts and evidence are available.

### DOC-003 — Scanner README overstates current operational certainty
- **Status:** Documentation corrected; scheduler state unverified.
- **Finding:** The prior README described a daily cron as running and pushing changes. The published pointer is next=10 and the available scan.log entries end 2026-10-26; those facts alone do not establish current scheduler state.
- **Action:** Document the cycle and published state without claiming the external scheduler is active or stopped. Reconcile scheduler configuration, execution history, pointer, and log before making an operational claim.

### DOC-004 — Research index and calibration may lag later proof/status records
- **Status:** Open; requires source-by-source reconciliation.
- **Finding:** Earlier research landing/calibration material marks the B-7 analytic equivariance proof incomplete, while Appendix P contains a B-7 twist lemma and later research notes make stronger status claims.
- **Action:** Compare each summary statement against the actual derivation, assumptions, and open-gate records. Do not promote the overall B-7 result unless the full required proof is present.

### DOC-005 — Manuscript README understated series scope
- **Status:** Addressed on this documentation branch.
- **Finding:** The prior README described the rewrite as Books 0–22 and Volumes 0–IV, and did not clearly delimit the original snapshot coverage.
- **Action:** State the current Books 0–24 scope, distinguish Volume 0 from chronological volumes, and explain that the listed original snapshots cover Books 0–19 only.

### DOC-006 — Backup mirror README and synchronization claims are stale
- **Status:** Open; mirror README needs refresh and content comparison.
- **Finding:** The selected backup mirror has historical owner/sync wording that does not reflect its current location and observed tree.
- **Action:** Describe it as the selected backup mirror, identify the primary repository as canonical, and record a sync date only after a real content comparison. Do not claim byte-for-byte parity without evidence.

## Infrastructure and provenance

### INF-001 — Database and registry snapshot counts need reconciliation
- **Status:** Open.
- **Finding:** A database README snapshot reports 1,141 theorem records, 199 dependency edges, and 283 terms; the status registry snapshot reports 195 records, including 86 attached to Books 2–6 and 109 unassigned. These are documented snapshot counts, not independently verified totals.
- **Action:** Recompute counts from the current SQL/schema and registry files; record source commit, generation command, timestamp, and inclusion rules.

### INF-002 — Referenced artifacts are missing from the reviewed tree
- **Status:** Open; locate or repair references.
- **Finding:** research/calibration.html references vol4/physics_interface/WITNESS_CANDIDATES.md, and Book 23 references an import-contract draft that was not found in the reviewed repository tree.
- **Action:** Search authoritative working sources. If unavailable, mark the reference unresolved or replace it with an existing canonical artifact; do not fabricate the missing documents.

## Research status and open gates

### RES-001 — Book 23 sector occupancy remains ASSERTED
- **Status:** Open research gate.
- **Finding:** Sector occupancy is explicitly labelled ASSERTED empirical content, not a derived result. The receiving block/bridge equations remain open.
- **Action:** Preserve the ASSERTED label until the missing equations, assumptions, and derivation are supplied and checked.

### RES-002 — Book 24 physical realization bridges remain open
- **Status:** Open research gate.
- **Finding:** Physical Oprop, E_k contact operators, the physical C8 action, and the ten-plane/measurement bridge remain unresolved in the reviewed status record.
- **Action:** Keep the physical interpretation conditional. Separate established conditional IO-word algebra from unproved physical operator and measurement claims.

## Editorial rule

A successful script run means only that the assertions implemented by that script passed. It does not establish that all manuscript claims are correct. Preserve distinctions among PROVED, CHECKED, ASSERTED, IMPORTED, INCOMPLETE/OPEN, and INCORRECT-AS-STATED. Record repository commits or external evidence for any future status change.
