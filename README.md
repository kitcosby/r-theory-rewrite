# R Theory — A Visual Rewrite

A book-by-book, intuition-first rewrite and audit companion for the *R Theory* manuscript. The repository currently contains Books 0–24 across Volumes I–V, plus a separate Volume 0 witness track. Visual explanations, live Desmos graphs, source references, and audit status are presented with the limits of each check disclosed.

## Read it

- Live site: <https://cosbykit-afk.github.io/r-theory-rewrite/>
- [Series contents](contents/) — book and section navigation
- [Series index](index/) — searchable A–Z index
- [Appendix P / proof materials](appendix-proofs/)
- [Research companion](research/)
- [Repository issue log](ISSUE_LOG.md)

The graphs use live [Desmos](https://www.desmos.com) calculators where available, with static PNG fallbacks in the relevant book folders. Live rendering should not be inferred from static repository checks.

## Series map

- **Volume I:** Books 0–6 (book0/–book6/)
- **Volume II:** Books 7–13 (book7/–book13/)
- **Volume III:** Books 14–16 (book14/–book16/)
- **Volume IV:** Books 17–19 (book17/–book19), *The Discrete Octant and the Computational Frontier*
- **Volume 0:** Books 20–22 (book20/–book22), a separate exact-witness track, not a chronological continuation of Volumes I–IV
- **Volume V:** Books 23–24, extending the rewrite beyond the earlier Books 0–22 inventory

Supporting areas include contents/ and index/ for navigation; tables/ and e8/ for supporting data; guide/ for *A Guide to Creative Reason (after Euclid)*; research/, appendix/, and appendix-proofs/ for research and proof-support material; validation/ for documented numerical and structural scripts; manuscript/ and pdf/ for source snapshots and exports; vol0/, vol4/, vol4-audit/, and title/ for supporting material; database/ for database exports and related artifacts; and scanner/ for scanner documentation, pointer, and published log.

## Evidence and status discipline

Status labels describe the kind and scope of evidence actually supplied; they are not interchangeable:

- **PROVED / CP:** a stated proof or exact derivation supports the claim within its stated assumptions and scope.
- **CHECKED / SC / NC:** symbolic or numerical checks support the specified calculation. A numerical check is not, by itself, a proof.
- **ASSERTED / MA:** a manuscript or research assertion that has not been derived or independently established in the repository.
- **INCOMPLETE / OPEN:** a required derivation, bridge, definition, or verification remains outstanding.
- **INCORRECT-AS-STATED / IC:** the claim fails as written, or requires qualifications not present in the original statement.
- **IMPORTED:** a result is cited from an external source; citation does not mean it has been independently reproved here.

Original manuscript labels (for example, CERTIFIED) are preserved as source labels and must not be mistaken for independent verification. Witness essays and candidate constructions are not, by themselves, new physical laws.

## Audit and coverage notes

- The documented validation inventory covers Books 0–19 and the Volume IV overview. It is not a complete validation inventory for Books 20–24; see validation/README.md.
- The Volume IV audit summary reports 407 assertions, including 18 incorrect-as-stated findings, with Δ_op(Volume IV) = ∅. A clean audit-script run does not mean the manuscript has no errors.
- Volume 0 is a distinct witness track. Its essays and exact witnesses should be read within their stated scope.
- Volume V contains conditional algebraic results and explicit empirical assertions. Book 23 sector occupancy is labelled ASSERTED, not derived. Book 24's physical operator/contact and measurement bridges remain open; consult the relevant book and research records before treating them as established physics.
- Database and registry counts are snapshot claims. They should be reconciled against the underlying data and provenance before being treated as independently verified totals.

## Source and mirror

This repository is the visual rewrite and audit companion; the original manuscript snapshots under manuscript/ are read-only references and are not complete copies of every book.

The selected backup mirror is [kitcosby/R-Theory](https://github.com/kitcosby/R-Theory). It is a backup mirror, not the canonical live-site source; do not assume byte-for-byte synchronization without a comparison.

## License

Public domain — [The Unlicense](LICENSE).
