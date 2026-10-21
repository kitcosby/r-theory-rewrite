#!/usr/bin/env python3
"""Volume II audit — Book 11, 11.PG.VI checks (O-11.1).

Claim under audit: within the declared candidate class (oriented Lorentzian
4-manifold, Hodge star, invariant inner product on su(2), no extra fields),
the standard local gauge-invariant two-derivative connection action is
unique up to the two constants g and theta:

    S = -(1/2g^2) int tr(F^*F) + theta int tr(F^F).

The classification has three steps:
  (0) Locality + gauge invariance => the density is a function of F and its
      covariant derivatives; DF = 0 identically (Bianchi), and D^k F (k>=1)
      exceeds two-derivative order. [written argument, recorded in the ledger]
  (1) A quadratic F-term needs an Ad-invariant symmetric bilinear form on
      su(2). Computed here exactly: the solution space is 1-dimensional.
  (2) In 4D the space of Lorentz-invariant quadratic scalar forms on a
      2-form F is exactly 2-dimensional, spanned by F_mn F^mn and
      eps^{mnrs} F_mn F_rs. Computed here exactly.

Checks (1) and (2) are exact rational linear algebra (CHECKED, exact).
Also verified: tr(T_a) = 0, so no single-trace / linear-F term exists.

Exit 0 iff all checks pass.
"""
import sympy as sp

results = []
def check(name, cond):
    results.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

# ---------- su(2): invariant bilinear forms ----------
# Real adjoint representation: (ad_a)_{bc} = eps_{bac} (generates SO(3)).
def eps(a, b, c):
    if (a, b, c) in [(0,1,2),(1,2,0),(2,0,1)]: return 1
    if (a, b, c) in [(0,2,1),(2,1,0),(1,0,2)]: return -1
    return 0
ad = []
for a in range(3):
    M = sp.zeros(3, 3)
    for b in range(3):
        for c in range(3):
            M[b, c] = eps(b, a, c)
    ad.append(M)

bij = sp.symbols('b0:6')
B = sp.Matrix([[bij[0], bij[1], bij[2]],
               [bij[1], bij[3], bij[4]],
               [bij[2], bij[4], bij[5]]])
eqs = []
for a in range(3):
    E = ad[a].T*B + B*ad[a]
    eqs += list(E)
sol = sp.solve(eqs, bij, dict=True)
free = set()
for s in sol:
    for v in bij:
        if v not in s:
            free.add(v)
check("D1 invariant symmetric bilinear forms on su(2): solution space is 1-dimensional",
      len(sol) == 1 and len(free) == 1)
Bsol = B.subs(sol[0])
check("D1b the unique invariant form is proportional to delta_ab (identity)",
      sp.simplify(Bsol - Bsol[0, 0]*sp.eye(3)) == sp.zeros(3, 3))

# tr(T_a) = 0 in the fundamental (Pauli/2): no linear-F invariant exists.
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.diag(1, -1)
T = [s1/2, s2/2, s3/2]
check("D2 tr(T_a) = 0 for all a (single-trace terms vanish identically)",
      all(sp.trace(Ta) == 0 for Ta in T))
check("D2b tr(T_a T_b) = (1/2) delta_ab (the invariant form in the fundamental)",
      all(sp.trace(T[a]*T[b]) == sp.Rational(1, 2)*(1 if a == b else 0)
          for a in range(3) for b in range(3)))

# ---------- Lambda^2(R^{1,3}): Lorentz-invariant quadratic forms ----------
eta = sp.diag(-1, 1, 1, 1)
basis = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]  # independent components of F_mn

def rho(X):
    """Induced action of a Lorentz-algebra matrix X (mixed indices) on Lambda^2.
    A covariant 2-form transforms F -> -(X^T F + F X) infinitesimally."""
    M = sp.zeros(6, 6)
    for j, (m, n) in enumerate(basis):
        F = sp.zeros(4, 4); F[m, n] = 1; F[n, m] = -1
        XF = -(X.T*F + F*X)
        for i, (p, q) in enumerate(basis):
            M[i, j] = XF[p, q]
    return M

# so(1,3) generators (mixed-index, eta-antisymmetric): rotations J_i, boosts K_i
gens = []
for i in range(1, 4):  # boosts K_i: X^0_i = X^i_0 = 1
    X = sp.zeros(4, 4); X[0, i] = 1; X[i, 0] = 1
    gens.append(X)
for (i, j) in [(1,2),(1,3),(2,3)]:  # rotations J_k: X^i_j = -X^j_i = 1
    X = sp.zeros(4, 4); X[i, j] = 1; X[j, i] = -1
    gens.append(X)
rhos = [rho(X) for X in gens]

mij = sp.symbols('m0:21')
idx = [(i, j) for i in range(6) for j in range(i, 6)]
Mm = sp.zeros(6, 6)
for k, (i, j) in enumerate(idx):
    Mm[i, j] = mij[k]; Mm[j, i] = mij[k]
eqs = []
for R in rhos:
    E = R.T*Mm + Mm*R
    eqs += list(E)
linsys = sp.linear_eq_to_matrix(eqs, list(mij))
rank = linsys[0].rank()
nullity = 21 - rank
check("D3 Lorentz-invariant symmetric bilinear forms on Lambda^2(R^1,3): space is 2-dimensional",
      nullity == 2)

# The two spanning forms: Q1(F) = F_mn F^mn, Q2(F) = eps^{mnrs} F_mn F_rs.
def gram(Q):
    G = sp.zeros(6, 6)
    for i, (m, n) in enumerate(basis):
        for j, (p, q) in enumerate(basis):
            Fi = sp.zeros(4, 4); Fi[m, n] = 1; Fi[n, m] = -1
            Fj = sp.zeros(4, 4); Fj[p, q] = 1; Fj[q, p] = -1
            G[i, j] = Q(Fi, Fj)
    return G
def Q1(F, G_):
    return sum(eta[m, m]*eta[n, n]*F[m, n]*G_[m, n] for m in range(4) for n in range(4))
eps4 = sp.LeviCivita
def Q2(F, G_):
    return sum(int(eps4(m, n, r_, s))*F[m, n]*G_[r_, s]
               for m in range(4) for n in range(4) for r_ in range(4) for s in range(4))
G1, G2 = gram(Q1), gram(Q2)
check("D3b Q1 and Q2 are linearly independent invariant forms (span the 2-dim space)",
      sp.Matrix.hstack(G1.reshape(36, 1), G2.reshape(36, 1)).rank() == 2
      and all(sp.simplify((R.T*G1 + G1*R)) == sp.zeros(6, 6) for R in rhos)
      and all(sp.simplify((R.T*G2 + G2*R)) == sp.zeros(6, 6) for R in rhos))

npass = sum(1 for _, ok in results if ok)
print(f"\nSUMMARY: {npass}/{len(results)} checks PASS -- all CHECKED (exact linear algebra)")
assert npass == len(results), "FAILURES PRESENT"
print("VERDICT: O-11.1 algebraic core CONFIRMED exactly (dims 1 and 2); "
      "classification step (0) is the written argument recorded in the ledger.")
