# Book 24 Two-Needle Dial — Equality and Blind Set

**Date:** 2026-11-05  
**Source:** Book 24 §2 and Appendix P §P-3, especially T1, T3, T4, and the cross-ratio identity.

## Scope and assumptions

The published candidate-model setup takes Z and γ as arbitrary real 368×556 matrices. The mass block is M_e = diag(m₀ I₃₆₈, m₂ I₅₅₆, M_rest); the archived reference values are m₀ = 2 and m₂ = 5, explicitly not physical selections. D_B contains M_e⁻¹, so m₀m₂ = 0 is outside the stated domain.

The P-3 closed forms are conditional on the stated sector projectors, the pure grade-flip ε-odd result, and the 12-dimensional Oprop candidate space. The page explicitly leaves the physical E_k and Oprop matrices open. This note derives consequences of the displayed closed forms; it does **not** re-audit the original T3/T4 block-operator derivations or identify physical observables.

## Exact algebraic classification

Set

~~~text
D8 = ||Zᵀ Z||_F²
C  = Tr(ZZᵀ γ Zᵀ Z γᵀ) ≥ 0

DW = 2 m₀ m₂ C + m₀² D8
DB = 2 (m₀ m₂)⁻¹ C + m₀⁻² D8
~~~

Multiplying the two displayed formulas gives

~~~text
DW DB − D8²
  = 4 C² + 2 (m₂/m₀ + m₀/m₂) C D8.
~~~

For the archived reference values m₀ = 2 and m₂ = 5,

~~~text
DW DB − D8² = 4 C² + (29/5) C D8 ≥ 0.
~~~

The same nonnegativity holds for any same-sign nonzero m₀,m₂, because m₂/m₀ + m₀/m₂ ≥ 2. If opposite-sign parameters were admitted, that AM–GM step would fail and the inequality would not follow in general. Zero parameters are excluded because DB uses M_e⁻¹.

Since ZᵀZ is positive semidefinite,

- D8 = 0 iff Z = 0.
- If Z ≠ 0, then D8 > 0.
- With m₀m₂ > 0, equality DW DB = D8² holds iff C = 0.
- Strictness holds iff C > 0.

Thus γ = 0 is sufficient for equality, but it is **not necessary**. The published phrase “strictness signals dressed-O content” needs the qualifier “support-visible”: strictness detects C > 0, not every nonzero γ.

## Exact blind-set characterization

Let Z = UΣVᵀ be a thin singular-value decomposition of rank r, with U and V having orthonormal columns and Σ positive diagonal. Then

~~~text
ZZᵀ = UΣ²Uᵀ
ZᵀZ = VΣ²Vᵀ
C = ||Σ Uᵀ γ V Σ||_F².
~~~

Because Σ is invertible on the rank-r support,

~~~text
C = 0  iff  Uᵀ γ V = 0
    iff  P_col(Z) γ P_row(Z) = 0,
~~~

where P_col(Z) and P_row(Z) are the orthogonal projectors onto the column and row spaces of Z.

The two-needle product is therefore blind to every γ whose block from the active right-singular support of Z to the active left-singular support is zero. γ may be nonzero outside that support block.

## Exact nonzero-γ equality witness

The following 2×2 corner block embeds by zero-padding into the published 368×556 matrix space:

~~~text
Z = [[1, 0],
     [0, 0]]

γ = [[0, 1],
     [0, 0]]
~~~

Then Z ≠ 0 and γ ≠ 0, but

~~~text
D8 = 1
C  = 0
DW = 4
DB = 1/4
DW DB = D8² = 1.
~~~

For comparison, keeping the same Z but taking γ = [[1,0],[0,0]] gives C = 1 and, at m₀ = 2, m₂ = 5,

~~~text
DW = 24
DB = 9/20
DW DB − D8² = 49/5 > 0.
~~~

These are exact witnesses, not a substitute for the SVD proof.

## Reproducible Lampy computation

Two inspected, pure exact-arithmetic jobs were submitted to the existing Gwen research queue. Neither job reads files, accesses the network, or modifies project data.

| Job | Engine | Version | Exit | Runtime |
|---:|---|---|---:|---:|
| 2719 | Python / SymPy | Python 3.10.12 / SymPy 1.14.0 | 0 | 0.36 s |
| 2720 | SageMath | SageMath 9.5 / Python 3.10.12 | 0 | 2.32 s |

Both engines independently reported:

~~~text
PASS symbolic gap factorization
PASS reference-mass gap coefficient
PASS nonzero-Z, nonzero-gamma blind witness (C=0, D8=1, DW*DB=1)
PASS visible witness (C=1, D8=1, gap=49/5)
~~~

Raw queue outputs are retained in gwen_training.calc_jobs for IDs 2719 and 2720. The jobs verify the symbolic multiplication and exact 2×2 examples. They do not prove the original block formulas or identify physical E_k/Oprop matrices.

## Evidence classification and required correction

- **Verified derivation:** the factorization, equality condition, and SVD blind-set characterization, conditional on the published T3/T4 closed forms and m₀m₂ > 0.
- **Computationally supported:** the exact symbolic identity and matrix witnesses, independently checked in SymPy and SageMath.
- **Counterexample found:** nonzero γ does not imply strictness.
- **Not established:** physical E_k/Oprop, the physical C8 action, or any dial-to-observable law.

The Book 24 page, Appendix P source fragment, assembled Appendix P page, and calibration page should state that equality is equivalent to C = 0, not γ = 0, and that the two-needle test sees only support-visible γ content. Existing PROVED/CHECKED labels and physical open gates are preserved.


## Fixed-Z kernel bound for the 12-dimensional candidate space (2026-11-06)

This is a rank-nullity result, not a numerical test. Assume the candidate space \(\mathfrak b\) is a 12-dimensional real linear subspace of \(\mathbb R^{368\times556}\), and, for this conditional statement, that \(\gamma\) ranges over \(\mathfrak b\). For a fixed nonzero \(Z\) of rank \(r\) with thin SVD \(Z=U\Sigma V^T\), define

~~~text
Phi_Z : b -> M_r(R)
Phi_Z(gamma) = U^T gamma V.
~~~

The SVD characterization already established gives \(C=0\iff\Phi_Z(\gamma)=0\). Since \(\dim M_r(\mathbb R)=r^2\), rank-nullity yields

~~~text
dim ker(Phi_Z) >= max(0, 12 - r^2).
~~~

Consequently, for every fixed \(Z\) of rank 1, 2, or 3, the 12-dimensional ansatz contains a nonzero blind element; the kernel dimension is at least 11, 8, or 3, respectively. For rank \(r\ge4\), dimension counting alone does not force a nontrivial kernel; injectivity is possible but has not been established for the actual ansatz.

This conclusion is conditional on \(\mathfrak b\) being the admissible linear space for the dial's \(\gamma\). It does not establish that a physical transfer matrix has rank at most 3, nor that the 12-dimensional candidate space is the final physical Oprop space. For a fixed physical \(Z\) of rank at least 4, the next test requires the actual 12 basis matrices and the physical \(Z\), then an exact rank computation for the resulting compression map. Those artifacts were not found in the searched public tree or Lampy workspace paths. No Gwen job was submitted: the rank-nullity argument is exact and a numerical run would add no evidence.
