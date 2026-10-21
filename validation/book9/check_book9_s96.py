#!/usr/bin/env python3
"""Volume II audit — Book 9, section 9.6 checks (O-9.1, O-9.2).

Exact symbolic computation (SymPy, no numerics) of the Einstein tensor for
Book 9's ansatze, from the definitions in the manuscript span:

  one-scalar reciprocal ansatz (9.4/9.6): ds2 = -f dt2 + f^-1 dr2 + r2 dOm2, f = N^2
  two-variable coframe (9.5):             ds2 = -N^2 dt2 + A^2 dr2 + r2 dOm2
  chart (9.6): q = (1-N)/(1+N), sigma = ln(A N)

Units c = 1. Einstein equation convention G^mu_nu = 8 pi T^mu_nu (G = 1),
T^t_t = -rho, T^r_r = p_r, T^th_th = p_th.

Scope: every check below is CHECKED (exact symbolic). Nothing here is an
analytic proof; the identities are verified by exact rational simplification
of the general expressions, which is the strongest label this computation earns.

Exit 0 iff all checks pass. Prints a scope-counted summary.
"""
import sympy as sp

t, r, th, ph = sp.symbols('t r th ph')
coords = [t, r, th, ph]
results = []

def check(name, cond):
    results.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

def einstein_mixed(g):
    n = 4
    ginv = g.inv()
    dg = [[[sp.diff(g[i, j], coords[k]) for k in range(n)] for j in range(n)] for i in range(n)]
    Gamma = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                expr = 0
                for d in range(n):
                    expr += ginv[a, d]*(dg[d][b][c] + dg[d][c][b] - dg[b][c][d])/2
                Gamma[a][b][c] = sp.simplify(expr)
    Ric = sp.zeros(n, n)
    for b in range(n):
        for d in range(n):
            expr = 0
            for a in range(n):
                expr += sp.diff(Gamma[a][b][d], coords[a])
                expr -= sp.diff(Gamma[a][b][a], coords[d])
                for e in range(n):
                    expr += Gamma[a][a][e]*Gamma[e][b][d] - Gamma[a][d][e]*Gamma[e][b][a]
            Ric[b, d] = sp.simplify(expr)
    R = sp.simplify(sum(ginv[i, j]*Ric[i, j] for i in range(n) for j in range(n)))
    G = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            G[i, j] = sp.simplify(Ric[i, j] - sp.Rational(1, 2)*g[i, j]*R)
    Gm = ginv*G
    return [sp.simplify(Gm[i, i]) for i in range(n)]

# ---------- Part A: one-scalar obstruction (O-9.2) ----------
f = sp.Function('f')(r)
fp = sp.diff(f, r)
G1 = einstein_mixed(sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2))
Gtt, Grr, Gth = G1[0], G1[1], G1[2]

check("A1 G^t_t - G^r_r == 0 identically (one-scalar constraint -rho = p_r)",
      sp.simplify(Gtt - Grr) == 0)
check("A2 G^t_t == (r f' + f - 1)/r^2 closed form",
      sp.simplify(Gtt - (r*fp + f - 1)/r**2) == 0)
check("A3 G^th_th == f''/2 + f'/r (tangential pressure fixed by f alone)",
      sp.simplify(Gth - (sp.diff(f, r, 2)/2 + fp/r)) == 0)

# Dust collapse: dust has p_r = p_th = 0, T^t_t = -rho.
# A1 + Einstein eq force rho = 0 and G^t_t = 0, i.e. r f' + f - 1 = 0 (9.4 vacuum eq).
# Its general solution f = 1 - C/r must also satisfy G^th_th = 0:
C = sp.symbols('C')
fvac = 1 - C/r
check("A4 vacuum branch f = 1 - C/r annihilates all of G (dust collapse target)",
      all(sp.simplify(G.subs(f, fvac).subs(sp.diff(f, r), sp.diff(fvac, r))
                      .subs(sp.diff(f, r, 2), sp.diff(fvac, r, 2))) == 0 for G in (Gtt, Grr, Gth)))

# ---------- Part B: sourced equation and Poisson scope (O-9.1) ----------
m = sp.Function('m')(r)
fm = 1 - 2*m/r
Gtt_m = sp.simplify(Gtt.subs(f, fm).subs(fp, sp.diff(fm, r)))
check("B1 f = 1 - 2m(r)/r  =>  G^t_t == -2 m'(r)/r^2 exactly (=> m' = 4 pi rho r^2 sourced eq)",
      sp.simplify(Gtt_m + 2*sp.diff(m, r)/r**2) == 0)

mu = sp.symbols('mu', positive=True)
Nv = sp.sqrt(1 - 2*mu)
q = (1 - Nv)/(1 + Nv)
ser = sp.series(q, mu, 0, 4).removeO()
check("B2 q = mu/2 + mu^2/2 + 5 mu^3/8 + O(mu^4), i.e. q = -Phi_ext/2 + O(Phi^2), Phi_ext = -mu",
      sp.simplify(ser - (mu/2 + mu**2/2 + 5*mu**3/8)) == 0)
check("B3 1 - N^2 == 4q/(1+q)^2 identically (ties q to 9.3 defect r(1-N^2) = 4a)",
      sp.simplify((1 - Nv**2) - 4*q/(1 + q)**2) == 0)
check("B3b with f = 1 - 2mu: 1 - N^2 == 2mu, so a = mu r / 2 (9.4 calibration a = GM/2c^2 at c=1)",
      sp.simplify((1 - Nv**2) - 2*mu) == 0)

M = sp.symbols('M', positive=True)
Phi_ext = -M/r
lap_Phi = sp.simplify((1/r**2)*sp.diff(r**2*sp.diff(Phi_ext, r), r))
check("B4 exterior potential Phi_ext = -M/r satisfies Laplace (Poisson, rho=0) for r > 0",
      lap_Phi == 0)

# Scope boundary (negative result, computed): the ansatz potential
# Phi_a = (f-1)/2 = -m(r)/r does NOT obey the interior Poisson equation.
Phi_a = -m/r
lap_Pa = sp.simplify((1/r**2)*sp.diff(r**2*sp.diff(Phi_a, r), r))
check("B5 nabla^2 Phi_a == -m''(r)/r (NOT 4 pi rho for general rho: interior pointwise Poisson fails)",
      sp.simplify(lap_Pa + sp.diff(m, r, 2)/r) == 0)

# ---------- Part C: second coframe variable (O-9.2 corollary) ----------
Nf = sp.Function('N')(r)
Af = sp.Function('A')(r)
G2 = einstein_mixed(sp.diag(-Nf**2, Af**2, r**2, r**2*sp.sin(th)**2))
D = sp.simplify(G2[0] - G2[1])
sigmap = sp.diff(sp.log(Nf*Af), r)
check("C1 two-variable: G^t_t - G^r_r == -2 sigma'/(r A^2), sigma = ln(A N)",
      sp.simplify(D + 2*sigmap/(r*Af**2)) == 0)
check("C2 A = 1/N recovers the one-scalar constraint (difference vanishes)",
      sp.simplify(D.subs(Af, 1/Nf).subs(sp.diff(Af, r), sp.diff(1/Nf, r))) == 0)

npass = sum(1 for _, ok in results if ok)
print(f"\nSUMMARY: {npass}/{len(results)} checks PASS -- all CHECKED (exact symbolic)")
assert npass == len(results), "FAILURES PRESENT"
print("VERDICT: O-9.2 obstruction CONFIRMED exactly; O-9.1 confirmed in exterior/"
      "integrated scope only (B5 boundary).")
