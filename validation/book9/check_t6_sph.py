#!/usr/bin/env python3
"""T6 audit checks, part 2: the spherical EH reduction (claim (c), T6.IV).

Metric (T6.I.1, signature +---): ds2 = N(r)^2 dt2 - A(r)^2 dr2 - r^2 dOm2.
Variables (T6.IV.1): F_g = A^-2, D_M = r(1 - F_g), sigma = ln(A N).
Action (T6.IV.2): S_EH = (1/2 kappa_g) int sqrt(-g) R d^4x.
Claim: after angular integration and removal of a radial boundary derivative,
  L_sph = (2 pi / kappa_g) e^sigma (D_M sigma' - D_M'),
vacuum EL equations D_M' = 0, sigma' = 0; momenta p_D = -C_g e^sigma,
p_sigma = C_g e^sigma D_M, constraint p_sigma + D_M p_D = 0, H_sph = 0;
source channels D_M' = kappa_g r^2 rho, sigma' = kappa_g r (rho+p_r)/(2 F_g).
All checks exact (SymPy). Ricci convention: R^a_{bcd} = d_c Gamma^a_{bd} - ...
(standard; the one under which the Schwarzschild mass sign comes out as below).
Exit 0 iff all checks pass.
"""
import sympy as sp

results = []
def check(name, cond):
    results.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

t, r, th, ph = sp.symbols('t r th ph')
coords = [t, r, th, ph]
Nf = sp.Function('N')(r); Af = sp.Function('A')(r)
g = sp.diag(Nf**2, -Af**2, -r**2, -r**2*sp.sin(th)**2)
ginv = g.inv(); n = 4
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
Gam = ginv*sp.Matrix([[sp.simplify(Ric[i, j] - sp.Rational(1, 2)*g[i, j]*R)
                       for j in range(n)] for i in range(n)])
Gtt, Grr = sp.simplify(Gam[0, 0]), sp.simplify(Gam[1, 1])

# Work with abstract derivative symbols for the reduction identity.
n0, n1, n2, a0, a1 = sp.symbols('N0 N1 N2 A0 A1')
sub = {sp.Derivative(Nf, (r, 2)): n2, sp.Derivative(Nf, r): n1, Nf: n0,
       sp.Derivative(Af, r): a1, Af: a0}
R_s = sp.simplify(R.subs(sub))
Gtt_s = sp.simplify(Gtt.subs(sub)); Grr_s = sp.simplify(Grr.subs(sub))

kap = sp.symbols('kappa_g', positive=True)
Cg = 2*sp.pi/kap
# T6 variables in (n0,a0,...) language:
esig = n0*a0                                   # e^sigma = A N
sgp = (n1*a0 + n0*a1)/(n0*a0)                   # sigma'
Dm = r*(1 - 1/a0**2)                            # D_M
Dmp = (1 - 1/a0**2) + 2*r*a1/a0**3              # D_M'
L_full = Cg * n0*a0*r**2 * R_s                  # (1/2k)*4pi*sqrt(-g) R dr-density
L_T6 = Cg * esig * (Dm*sgp - Dmp)
B = 2*r**2*n1/a0 - Dm*esig                      # candidate boundary function
Bp = (4*r*n1/a0 + 2*r**2*n2/a0 - 2*r**2*n1*a1/a0**2
      - (Dmp*esig + Dm*(n1*a0 + n0*a1)))
check("S1 full EH density minus T6's L_sph is exactly the radial derivative of "
      "B = 2 r^2 N'/A - D_M e^sigma (reduction exact modulo boundary, sign incl.)",
      sp.simplify(L_full - L_T6 - Cg*Bp) == 0)
check("S2 G^t_t = D_M'/r^2 exactly (mass-defect channel)",
      sp.simplify(Gtt_s - Dmp/r**2) == 0)
check("S3 G^t_t - G^r_r = 2 sigma'/(r A^2) exactly (strain channel)",
      sp.simplify((Gtt_s - Grr_s) - 2*sgp/(r*a0**2)) == 0)
rho, pr = sp.symbols('rho p_r')
Fg = 1/a0**2
# Under G^mu_nu = kappa_g T^mu_nu with T^t_t = rho, T^r_r = -p_r (static fluid,
# +---): S2 gives D_M' = r^2 G^t_t = kappa_g r^2 rho directly, and S3 gives
# sigma' = (r A^2/2)(G^t_t - G^r_r) = (r A^2/2) kappa_g (rho + p_r); the only
# algebra left is the A^2 = 1/F_g conversion in T6's stated sigma' channel:
check("S4 Einstein-eq conversion: (r A^2/2) kappa_g (rho+p_r) equals "
      "kappa_g r (rho+p_r)/(2 F_g) exactly (T6.IV.4 source channels)",
      sp.simplify((r*a0**2/2)*kap*(rho + pr) - kap*r*(rho + pr)/(2*Fg)) == 0)

# Downstream algebra of the stated L_sph: EL equations, momenta, constraint, H.
DmF = sp.Function('D_M')(r); sgF = sp.Function('sigma')(r)
L = Cg*sp.exp(sgF)*(DmF*sp.diff(sgF, r) - sp.diff(DmF, r))
EL_Dm = sp.simplify(sp.diff(sp.diff(L, sp.diff(DmF, r)), r) - sp.diff(L, DmF))
EL_sg = sp.simplify(sp.diff(sp.diff(L, sp.diff(sgF, r)), r) - sp.diff(L, sgF))
check("S5 Euler eq. for D_M in L_sph is -2 C_g e^sigma sigma' = 0, i.e. sigma' = 0",
      sp.simplify(EL_Dm + 2*Cg*sp.exp(sgF)*sp.diff(sgF, r)) == 0)
check("S6 Euler eq. for sigma in L_sph is 2 C_g e^sigma D_M' = 0, i.e. D_M' = 0",
      sp.simplify(EL_sg - 2*Cg*sp.exp(sgF)*sp.diff(DmF, r)) == 0)
pD = sp.diff(L, sp.diff(DmF, r)); psg = sp.diff(L, sp.diff(sgF, r))
check("S7 momenta p_D = -C_g e^sigma, p_sigma = C_g e^sigma D_M; constraint "
      "p_sigma + D_M p_D = 0; H_sph = p_D D_M' + p_sigma sigma' - L = 0",
      sp.simplify(pD + Cg*sp.exp(sgF)) == 0
      and sp.simplify(psg - Cg*sp.exp(sgF)*DmF) == 0
      and sp.simplify(psg + DmF*pD) == 0
      and sp.simplify(pD*sp.diff(DmF, r) + psg*sp.diff(sgF, r) - L) == 0)

npass = sum(1 for _, ok in results if ok)
print(f"\nSUMMARY: {npass}/{len(results)} checks PASS")
assert npass == len(results), "FAILURES PRESENT"
