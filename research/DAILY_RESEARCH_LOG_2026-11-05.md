# Daily R Theory Research Run — 2026-11-05

## Run metadata
- Primary repository: https://github.com/kitcosby/r-theory-rewrite
- Owner/account: kitcosby
- Branch inspected: main
- Main SHA: `57d46eaf8b4c91cb9ac75c3a784490b0af679c8e`
- Repository working tree on Lampy: main matches origin/main; two local untracked research-program files remain (`research/RESEARCH_PROGRAM.md`, `research/LAMPY_PIPELINE.md`). They were not committed or included in this change.
- Lampy access: verified via authorized TOE remote connection; WSL2 distribution running.
- Research program and pipeline adapter: present under `/usr/local/gwen-pipeline/`.
- No computation job submitted in this run.

## GitHub monitoring
- PR #4, “Clarify R Theory audit boundaries and Works Cited,” is merged. It clarifies the Books 20–24 / Volumes 0–V scope and validation boundary.
- No open GitHub issues were returned for the primary repository.
- Eight non-main remote branches were audited against main:
  - Ancestors of main (five): `archive/docs-2026-11-04-readme-and-issue-log`, `archive/docs-readme-and-issue-log-2026-11-04`, `docs/2026-11-04-readme-and-issue-log`, `docs/readme-and-issue-log-2026-11-04`, `readme-issue-log-2026-11-04`.
  - Divergent/stale (three): `docs/repo-map-2026-11-04` (main ahead 2, branch ahead 1; its unique commit is patch-equivalent to main, while the branch's remaining tree difference is a 4-line series-index change); `recovery/book23-orphaned` (main ahead 58, branch ahead 1; unique commit is not patch-equivalent and its Book 23 page is an older, much shorter snapshot); `site-dist` (main ahead 156, branch ahead 54, no merge base; separate historical site history).
- No branches were merged or deleted. No changes were pushed to main.

## Selected investigation — RES-001 / Book 23 sector occupancy
### Question
Can the imaginary-negative-volume sector assignment be independently established through the current C-1 physical interface?

### Source review
- `book0/index.html` §15, Theorem 0.III.T1 — Representation–Preference Separation.
- Original source: `manuscript/R-Theory-Volume-I-original.txt`, Theorem 0.III.T1.
- `book0/index.html` Corollary 0.III.C2.
- `book23/index.html` §§2–5.
- `book23/CHIRAL-ANCHOR-01.json` and `book23/CHIRAL-ANCHOR-02.json`.
- `research/calibration.html` anchor/dial description.

### Findings
1. Theorem 0.III.T1 is explicitly scoped to revised M0–M4 and admitted T0–T3 orientation transformations. It says these structures represent orientation but do not derive a preferred physical chirality.
2. Corollary 0.III.C2 permits a later physics-interface interaction, observable, source, boundary condition, or preparation law to distinguish alternatives. Thus the theorem does not prohibit every possible physical extension; it prohibits selection from the admitted candidate universe alone.
3. Book 23 and CHIRAL-ANCHOR-02 correctly label sector occupancy ASSERTED-by-Kit and explicitly say it is not derived from the mathematics.
4. The 21 cm hyperfine line and Zeeman σ polarization provide real scale and field-sensitive polarization measurements. The repository does not yet publish a map from Stokes/Zeeman sign or line-of-sight field to `sign(Re(z) * Im(z))`.
5. The C-1 receiving block and bridge equations remain open. The referenced `vol4/physics_interface/IMPORT_CONTRACTS_DRAFT.md` is absent from the public repository; INF-002 already records this.
6. Therefore RES-001's “derived from core operators” closure route needs scope clarification: it can only be pursued as an explicitly declared extension/physical input outside the candidate universe of 0.III.T1. No derivation or status promotion was performed. RES-001 remains Open.
7. Candidate symmetry audit: if the relevant observable is (B_{los}=\mathbf B\cdot\hat n), then under standard transformations `B` is axial (P-even, T-odd) and `n` is polar (P-odd, T-even), making `B_los` P-odd and T-odd. This is a local, field-dependent quantity; whether it can encode a global sector preference requires an explicit, convention-invariant bridge. This is a mathematical/physics inference to test, not a result established by the cited papers.

### Classification
- Theorem 0.III.T1 statement: established within the manuscript's stated candidate universe; proof audit not repeated in this run.
- CHIRAL-ANCHOR-02 occupancy: ASSERTED-by-Kit, not derived.
- 21 cm hyperfine/Zeeman readout: imported/established physical background.
- Mapping from Zeeman/Stokes data to R Theory sector sign: OPEN / not established.
- No computational verification performed.

## Consensus and primary literature
Consensus searches covered 21 cm Zeeman polarization, Stokes V measurement, parity violation, and chirality/order-parameter formulations. Full paper records were fetched for the cited candidates; full source inspection is reflected in the Works Cited update.
- Direct method match: Cooray & Furlanetto (2005), MNRAS Letters 359(1), L47–L52, DOI 10.1111/j.1745-3933.2005.00035.x; full publisher article inspected. Establishes Zeeman σ components' opposite circular polarizations and use of differential polarization to probe line-of-sight fields; does not establish an R Theory sector map.
- Measurement caveat: Wolfe et al. (2011), ApJ 733(1), 24, DOI 10.1088/0004-637X/733/1/24; full arXiv paper inspected. A phase/software error confused Stokes V with Stokes U and invalidated a prior claimed Zeeman detection.
- Related parity context: Quack, Seyfang & Wichmann (2022), Chemical Science 13(36), 10598–10643, DOI 10.1039/D2SC01323A; full open-access review inspected. Predicted parity-violating molecular energy differences had not yet been experimentally detected at publication.
- Related order parameter: Kishine, Kusunose & Yamamoto (2022), Israel Journal of Chemistry 62(11–12), e202200049, DOI 10.1002/ijch.202200049; full article inspected. Proposes electric toroidal monopole G0 as a molecular/crystal chirality order parameter and discusses enantioselective fields; not a universal selector for R Theory's carrier.
- Physical constants background: Furlanetto (2019), “Theoretical Framework: The Fundamentals of the 21 cm Line,” chapter 1, DOI 10.1088/2514-3433/ab4a73ch1; full chapter inspected.
- Pending full-text verification: Troland & Heiles (1982); Barron (2013); Xu et al. (2026). These remain leads, not promoted references.
- No direct literature match was found for the exact map `sign(Re(z) * Im(z))` from a 21 cm Zeeman/Stokes observable.

## Works Cited
- Existing page format inspected.
- Five full-text-verified sources added, with claim-specific R Theory mappings, evidence locators, DOIs/stable URLs, and explicit scope limitations.
- Furlanetto 2019 arXiv lead promoted to a complete verified citation.
- van de Hulst H I notes source located; author/editor/date metadata still incomplete, so it remains a lead.
- Wikipedia remains a tertiary background lead only.
- Pending full-text leads (Troland & Heiles 1982, Barron 2013, Xu et al. 2026) recorded separately.
- No claim that these sources prove R Theory's sector assignment.

## Lampy / compute queue
- WSL2 Lampy accessible; repository clean relative to main except the two untracked local program/adapter files noted above.
- Gwen pipeline RUNNING under exactly one Supervisor instance.
- PostgreSQL queue responsive.
- Historical queue totals at check: 1,466 completed jobs (Python 764, Sage 73, SQL 320, Wolfram 309) and 24 failed jobs (Python 17, SQL 7). These are lifetime queue totals, not work performed in this run.
- No new queue job was staged or run.

## Notion reconciliation
- Project Board and Board guide last edited 2026-09-19.
- Open Issues database contains OI-01…OI-29 (28 rows returned); the current rows are all marked Open and the Volume field covers Vol I / Cross-volume. It contains no RES-001 or RES-002 entries and no Book 23/24 or Vol V records.
- Critical Path contains CP-01…CP-13; CP-13 is Book 19 audit marked Complete. The guide explicitly describes only OI-01…OI-29, CP-01…CP-13, and IC-1…IC-18.
- The existing Notion board therefore does not represent the newer GitHub Book 23/24 research state. No existing Notion issue or status was altered; no Volume V row was created because the current database schema has no such option.
- Notion connected-source search was not available in the current access map; workspace page search/fetch and database reads were available.

## Next priority
1. Recover or publish the missing C-1 import contract/receiving block and specify the observable map from calibrated Zeeman/Stokes data to the sector sign.
2. State invariance requirements under line-of-sight reversal, polarization-convention changes, coordinate/frame reversal, and local magnetic-field reversal.
3. Decide whether the “core operators” closure route for RES-001 means a new physical extension outside 0.III.T1's candidate universe; otherwise obtain the explicit drop/ruling required by the issue's closure criteria.
4. Resume RES-002 only after the Book 24 physical Oprop/Ek/C8 and dial-identification dependencies are precisely mapped.
