# State of R Theory — Baseline Report
**Baseline date:** 2026-11-05  
**Primary source:** [kitcosby/r-theory-rewrite](https://github.com/kitcosby/r-theory-rewrite), branch `main`, commit `c9f3b9073a6eb066b2d537680d79fa3853e5dbf8`.

## Executive assessment

This is the first consolidated state report found in the repository. No prior document with this scope was found in the GitHub tree or the connected Notion search. The existing [research index](index.html) is explicitly an Una-operator-theory page and warns that Una results do not become R Theory results without a derivation; it is not a substitute for an R Theory state report.

R Theory is currently a **layered rewrite and research corpus**, not one globally closed axiom system. The first six books establish a mathematical spine and then introduce an explicit R-specific axiom. Later books add physical, representation-theoretic, and computational programs with different assumptions and evidence standards. Those layers must not be flattened into a single claim that “the theory is proved.”

This report is a baseline, not a theorem-by-theorem certification. The available registers and validation folders do not yet provide a complete global inventory for Books 0–24. The limitations are stated below rather than filled by inference.

## 1. Structural map

| Track | Books | Role in the corpus | Current evidence boundary |
|---|---:|---|---|
| Volume I | 0–6 | Source boundary, mathematical constitution, scalar R-operator calculus, projective phase, geometric carrier, Axiom Zero, local symmetry | Books 0–1 state the inherited scope and proof-status grammar. Books 2–6 have the structured claim registers. |
| Volume II | 7–13 | Classical dynamics, pre-Maxwell field geometry, relativity/gravity, quantum kinematics, particle architecture, mass calibration, thermodynamics/information | Per-book validation scripts exist. Their checks cover the assertions implemented by each script, not every claim in the manuscript. |
| Volume III | 14–16 | Two-fermion mass geometry, E8 bridge, microscopic theory | Per-book validation scripts exist; multiple physical and microscopic gates remain open. |
| Volume IV | 17–19 | Discrete octant, contraction module, UV boundary | Per-book validators and a Volume IV overview exist. The representation, normalization, and S_F/N_1820 gates remain open. |
| Volume 0 | 20–22 | Exact witnesses at the physics boundary | Present in the site tree, but not represented by equivalent per-book validation folders in the published validation inventory. |
| Volume V | 23–24 | Book 23 C-1 chirality/physics interface; Book 24 IO-word and dial campaign | The pages contain important conditional and asserted results, but no equivalent per-book validation folders are documented. Physical witness and measurement identifications remain open. |

Book numbering is not chronological volume numbering: Books 20–22 are Volume 0, while Books 23–24 are Volume V.

### Supporting infrastructure

- The [research ledger](../ledger/) and [status registry](../status_registry.json) provide claim-level status data, but the structured status registry covers Books 2–6 rather than the whole series.
- The [derivations registry](../derivations_registry.json) maps 86 audited claims and 39 Appendix P results (P-1 through P-6). It is not a complete series-wide theorem registry.
- The [database snapshot](../database/README.md), refreshed 2026-11-04, records 1,141 theorem rows, 199 dependency edges, and 283 terms. These counts describe a separate database artifact; they are not interchangeable with the 195 status-registry claims or the 86 derivation-map claims.
- The [validation inventory](../validation/README.md) documents scripts for Books 0–19 and the Volume IV overview. It explicitly does not claim equivalent coverage for Books 20–24. The listed suites were independently rerun on 2026-09-19; a successful script run proves only that its implemented checks passed.
- The [Works Cited page](../works-cited/) separates verified references, source leads, literature matches, and pending full-text checks.

## 2. Definitions and assumptions

### Book 0 spine

Book 0 admits the historical T0–T3 Projection Craft corpus as its sole inherited source corpus and audits it into four revised mathematical layers:

- **M0 — inherited background:** ordinary real analysis, trigonometry, and elementary topology. Book 0 states that M0 contributes no R-specific axiom.
- **M1 — scalar kernel:** the scalar transfer and reciprocal-odds calculus inherited from T0.
- **M2 — projection/readout firewall:** projection, observation, readout, rank, provenance, and calibration/validation distinctions. It does not itself select physical chirality.
- **M3 — orientation representation:** internal orientation machinery, including the orientation-relative orthogonal complex structure on a declared Euclidean two-plane. Reversing orientation exchanges J and −J; the representation does not privilege one choice.
- **M4 — geometric carrier:** the rank-three geometric carrier, Gram geometry, and coframe structure. Orientation can be represented once declared; the carrier metric alone does not prefer it.

Theorem 0.III.T1, Representation–Preference Separation, is scoped to revised M0–M4 and the admitted T0–T3 transformations. It does not establish a universal physical no-preference theorem. Corollary 0.III.C2 explicitly leaves room for a later physics-interface interaction, observable, source, boundary condition, or preparation law to distinguish alternatives.

### Book 1 constitution

Book 1 freezes M0–M4 as its source boundary, fixes a narrowest-valid-domain rule, and prohibits status promotion or import-smuggling. Its page reports zero new axioms, zero external imports, zero projection contracts, and zero physical claims at that stage. This is a boundary declaration, not evidence that later books contain no imports.

### First R-specific axiom

Book 5 introduces **Axiom Zero**: primitive diagonal noncoupling of a doubled carrier. The Decadic Carrier Theorem (real dimension 10 = 5 + 5) is a consequence **conditional on Axiom Zero**. Book 5 explicitly says the axiom is assumed, not proved. Any conclusion depending on the decadic carrier inherits that condition unless an independent derivation discharges it.

### Later extensions

Books 6 onward introduce local symmetry, representation theory, physical models, and empirical interfaces. Standard imported mathematics, manuscript assertions, model assumptions, numerical checks, and R Theory derivations must remain separately labelled. In particular, an imported representation decomposition or a numerical fit does not establish a new R Theory selection principle.

## 3. Claim and evidence inventory

The current structured status registry contains **195 claims**, with the following counts:

| Registry code | Count | Interpretation |
|---|---:|---|
| CP | 89 | Checked proof in the repository's audit vocabulary |
| SC | 30 | Symbolic/standard result in the registry's vocabulary |
| NC | 54 | Completed numerical check; not a proof |
| ST | 2 | Standard imported theorem/result |
| MA | 1 | Manuscript assertion or stipulation |
| IN | 6 | Incomplete |
| IC | 13 | Incorrect |

These 195 entries are concentrated in Books 2–6. The 86 claims and 39 results in the derivations registry are a different, overlapping register. The 1,141-row theorem database is a third artifact. A complete claim-ID crosswalk among these three sources has not been established.

The book-level evidence map is therefore:

- **Books 0–1:** foundational statements and scope controls are presented in the pages; this run did not repeat every proof audit.
- **Books 2–6:** the most structured claim-level audit is available through the 195-entry registry and the derivation map. Book 5's Axiom Zero remains an assumption even where its consequences are checked.
- **Books 7–19:** per-book validators and audit ledgers exist. They mix checked proofs, standard imports, numerical checks, manuscript assertions, incomplete items, and incorrect items. Script success must not be promoted to universal theorem validity.
- **Books 20–22:** exact-witness track; no equivalent per-book validation folders are documented in the current public inventory.
- **Book 23:** sector occupancy is explicitly ASSERTED-by-Kit. The 21 cm/Zeeman readout supplies physical scale and field-sensitive polarization, but the public repository does not yet provide the C-1 receiving block and convention-invariant map from the measured observable to the claimed sector sign.
- **Book 24:** Appendix P's dial theorems are conditional on the stated sector witnesses, the pure grade-flip theorem, and the 12-dimensional Oprop candidate space. The pages explicitly say the physical E_k and Oprop matrices remain open. The dials are therefore candidate-model requirements/attainability results, not a completed physical measurement law.

## 4. Dependency map

The following is a **navigation map**, not a verified theorem-dependency DAG:

1. M0 supplies ordinary mathematical background.
2. T0–T3 are audited into M1–M4 in Book 0.
3. Book 1 freezes that spine and its status/domain rules.
4. Book 2 names the canonical R-operator calculus and half-angle atlas.
5. Book 3 develops projective phase, orientation, and lift structure.
6. Book 4 develops geometric rank, coframes, and connection data.
7. Book 5 adds Axiom Zero and the conditional doubled/decadic carrier.
8. Book 6 develops local symmetry and carrier representation structure.
9. Books 7–13 develop physical applications; Books 14–16 extend the fermion/E8/microscopic program.
10. Books 17–19 develop the discrete-octant/contraction/UV frontier.
11. Books 20–22 form a parallel exact-witness track.
12. Books 23–24 attempt physical-interface and IO-word/dial connections.

Two dependencies have unusually high downstream impact:

- **Book 5:** the decadic carrier depends on Axiom Zero; it is not an unconditional theorem.
- **Volume IV/V physical interface:** the S_F/N_1820 chain depends on a correctly typed representation map, projectors, normalization, and physical witnesses. The Book 23 sector claim separately requires an observable contract outside Book 0's candidate universe.

## 5. Current proof gaps and contradictions

1. **Axiom Zero:** remains a declared R-specific assumption. Its consequences may be proved conditionally, but the axiom itself is not derived.
2. **Physical orientation:** Book 0 proves representability and scoped non-preference within M0–M4/T0–T3. It does not choose physical chirality.
3. **Book 23 sector occupancy:** remains ASSERTED. No published C-1 receiving block or invariant bridge maps the Zeeman/Stokes sign to sign(Re(z) Im(z)).
4. **Book 24 physical operators:** E_k, Oprop, the physical C8 action, and dial-to-observable identifications remain open.
5. **Book 24 two-needle interpretation:** the closed forms imply a support-sensitive equality condition, not “equality iff γ = 0.” The exact blind set and counterexample are documented in [the focused equality audit](BOOK24_TWO_NEEDLE_EQUALITY.md). The original T3/T4 block derivations were not re-audited in this run.
6. **P_54 / 1820 / 135:** the standard SO(10)×SU(4) branching places the 54 in the 135, not as a linear constituent of the 1820. The manuscript describes an active route through a quadratic 1820-to-135 map followed by P_54, but the explicit map/projector and its normalization are not constructed. The current skeleton's “54×54 or embedding in 1820” input is inconsistent with that route, and the existing skeleton does not apply P_54.
7. **S_F and N_1820:** the numerical gate remains open; the v1 skeleton's bare-trace computation is not the 54-projected S_F. No numerical result should be promoted until the missing E/B/O/F_C8/Q4/P_54 inputs and repaired template are supplied.
8. **Volume IV normalization/branching:** the N_1820 one-half-to-one-quarter gap, explicit Lambda²(16)-to-1820 branching, P_6435, ζ_parent, η_-4, c_ord, and K_parent remain live dependencies.
9. **Global traceability:** the 195-claim registry, 86-claim derivation map, and 1,141-row database snapshot have not been reconciled into a single series-wide claim inventory.
10. **Validation boundary:** equivalent public validation folders for Books 20–24 are not documented. Their page labels must not be treated as if the Books 0–19 validation suites had covered them.

## 6. Literature and novelty assessment

The current Works Cited is strongest around the Book 23 physical interface: the 21 cm line, Zeeman/circular-polarization methods, instrumental Stokes caveats, molecular parity violation, and chirality/order-parameter literature. Five sources were recorded as full-text verified in the preceding research cycle; additional leads remain segregated pending metadata or full-text verification.

This is not yet a comprehensive novelty review of the mathematical core. The next literature pass should map exact R Theory claims against standard sources in real/projective geometry, operator and matrix analysis, representation theory, Clifford/Spin structures, tensor decompositions, and E8 representation theory. Imported results must be identified as imports; analogies and shared notation are not theorem correspondences.

For the current Book 24 investigation, Consensus searches for positive-semidefinite trace inequalities and Frobenius/singular-value inequalities returned general background leads, not a direct match to the exact dial blind-set question. The fetched records did not provide sufficient full-text evidence for a claim-specific citation. No new Works Cited entry was added.

## 7. Ten prioritized investigations

1. **Construct the P_54/Q4 representation bridge.** Define and verify the quadratic map from Sym²(1820) into 135 and the rank-54 projector inside 135; reconcile the skeleton and all notation.
2. **Reconcile the N_1820 one-half-to-one-quarter gap.** Recompute the exact projectors, ranks, and normalization under the admitted embedding.
3. **Derive the Lambda²(16)-to-1820 branching and downstream E8/A7 maps.** Separate exact representation identities from model choices.
4. **Build or rule out the Book 23 C-1 receiving block.** Specify the observable, convention changes, parity/time-reversal behavior, and the map to the claimed sector sign.
5. **Complete the Book 24 physical witness/measurement bridge.** Identify E_k, Oprop, the C8 action, and each dial-to-observable contract without promoting candidate models.
6. **Audit the Book 16 A_y/R2R3/Airy/conjugacy gates.** Resolve attribution and exact operator dependencies before extending the microscopic program.
7. **Independently verify the Book 20 beta/Coulomb two-angle half-angle bridge.** Check domains, limiting cases, and source assumptions.
8. **Independently verify Book 21 color-singlet/SU(3) closure and the two-fermion invariant.** Check tensor symmetries and bound-mass limits.
9. **Verify the Book 22 symplectic atlas.** Prove chart domains, transition identities, seam limits, and degeneracies.
10. **Complete the global theorem/assumption/import registry and novelty map for Books 0–24.** Reconcile page claims, the two registries, database rows, validation scripts, and primary literature.

## 8. First research task and success criterion

**Task:** construct the exact Volume IV representation chain

~~~text
Sym²(1820) --Q4--> 135 --P_54--> 54
~~~

with the relevant SO(10)×SU(4) action, explicit basis conventions, normalization, and source-located definitions.

**Success criterion:** provide an explicit equivariant Q4 and rank-54 P_54 (or an equivalent inclusion/projection pair), verify the map's domain/codomain and intertwining identities, verify the projector's idempotence/rank, and show exactly where it enters S_F. If the required equivariant map does not exist under the stated representations, produce a scoped no-go proof and identify the minimal changed assumption. Until this is met, keep the S_F/N_1820 numerical gate OPEN.

---

**Status discipline:** this report records what the repository currently states and what this run checked. It does not certify every theorem, convert numerical checks into proofs, promote manuscript assertions, or claim physical selection.
