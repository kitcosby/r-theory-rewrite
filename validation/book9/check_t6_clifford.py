#!/usr/bin/env python3
"""T6 audit checks, part 1: Clifford core of T6.V Part D (claims (a),(b)).

Conventions (Dirac representation, signature +---):
  gamma^0 = diag(I,-I), gamma^i = [[0,sigma_i],[-sigma_i,0]],
  gamma_5 = i gamma^0 gamma^1 gamma^2 gamma^3,
  sigma^{ab} = (i/2)[gamma^a, gamma^b],  eps^{0123} = +1.
All matrix checks exact (sympy, entries in Q(i)).
Fierz checks exact on random rational spinors.
EC elimination exact symbolic algebra in the variables T6 states.
Exit 0 iff all checks pass.
"""
import itertools
import random
import sympy as sp

results = []
def check(name, cond):
    results.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

I2 = sp.eye(2); Z2 = sp.zeros(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
def blk(a, b, c, d):
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))
gam = [blk(I2, Z2, Z2, -I2),
       blk(Z2, s1, -s1, Z2),
       blk(Z2, s2, -s2, Z2),
       blk(Z2, s3, -s3, Z2)]
eta = sp.diag(1, -1, -1, -1)
gam_lo = [eta[a, a]*gam[a] for a in range(4)]  # gamma_a (no sum)
g5 = sp.simplify(sp.I*gam[0]*gam[1]*gam[2]*gam[3])

check("C0 Clifford: {gamma^a,gamma^b} = 2 eta^{ab} for all a,b",
      all(sp.simplify(gam[a]*gam[b] + gam[b]*gam[a] - 2*eta[a, b]*sp.eye(4)) == sp.zeros(4, 4)
          for a in range(4) for b in range(4)))
check("C0b gamma_5^2 = I and {gamma_5,gamma^a} = 0",
      sp.simplify(g5*g5 - sp.eye(4)) == sp.zeros(4, 4) and
      all(sp.simplify(g5*gam[a] + gam[a]*g5) == sp.zeros(4, 4) for a in range(4)))

def sigma_ab(a, b):
    return sp.simplify(sp.I/2*(gam[a]*gam[b] - gam[b]*gam[a]))

def eps4(a, b, c, d):
    p = [a, b, c, d]
    if len(set(p)) < 4: return 0
    inv = sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j])
    return -1 if inv % 2 else 1

# {gamma^c, sigma^{ab}}: exact structure. Coincident c in {a,b} -> 0;
# distinct c,a,b -> coeff * eps^{cabd} gamma_d gamma_5 with one constant coeff.
coeffs = set()
ok_all = True
for c in range(4):
    for a in range(4):
        for b in range(a+1, 4):
            A = sp.simplify(gam[c]*sigma_ab(a, b) + sigma_ab(a, b)*gam[c])
            if c in (a, b):
                if A != sp.zeros(4, 4): ok_all = False
                continue
            d = list({0, 1, 2, 3} - {c, a, b})[0]
            target = eps4(c, a, b, d)*gam_lo[d]*g5
            ratio = None; good = True
            for i in range(4):
                for j in range(4):
                    tij = sp.simplify(target[i, j]); aij = sp.simplify(A[i, j])
                    if tij == 0:
                        if aij != 0: good = False
                    else:
                        rij = sp.simplify(aij/tij)
                        if ratio is None: ratio = rij
                        elif rij != ratio: good = False
            if not good: ok_all = False
            else: coeffs.add(ratio)
check("C1 {gamma^c, sigma^{ab}} = 0 for c in {a,b}, and = coeff * eps^{cabd} gamma_d gamma_5 "
      "for distinct indices, all 24 (c,a<b) (T6's axial-channel identity)", ok_all)
check("C1b proportionality coefficient is a single constant across all distinct-index choices",
      len(coeffs) == 1)
COEF = coeffs.pop() if len(coeffs) == 1 else None
print("   coefficient found: {gamma^c,sigma^{ab}} =", COEF, "* eps^{cabd} gamma_d gamma_5"
      "  [sigma^{ab}=(i/2)[gamma^a,gamma^b], gamma_5=i g0 g1 g2 g3, eps^{0123}=+1]")

# Fierz identities on random rational spinors (exact).
random.seed(20261021)
def rand_spinor():
    return sp.Matrix([sp.Rational(random.randint(-3, 3)) + sp.I*sp.Rational(random.randint(-3, 3))
                      for _ in range(4)])
fierz_ok = True
spin_ok = True
for _ in range(8):
    psi = rand_spinor()
    if psi == sp.zeros(4, 1): continue
    psibar = (psi.conjugate().T)*gam[0]
    J = [sp.simplify((psibar*gam[a]*psi)[0]) for a in range(4)]
    K = [sp.simplify((psibar*gam[a]*g5*psi)[0]) for a in range(4)]
    S = sp.simplify((psibar*psi)[0])
    P = sp.simplify((sp.I*psibar*g5*psi)[0])
    JdotK = sum(eta[a, a]*J[a]*K[a] for a in range(4))
    J2 = sum(eta[a, a]*J[a]**2 for a in range(4))
    K2 = sum(eta[a, a]*K[a]**2 for a in range(4))
    if not (sp.simplify(JdotK) == 0 and sp.simplify(J2 + K2) == 0
            and sp.simplify(J2 - (S**2 + P**2)) == 0):
        fierz_ok = False
    # spin tensor tau^{abc} = psibar {gamma^a, sigma^{bc}} psi must be COEF * eps^{abcd} K_d
    K_lo = [eta[a, a]*K[a] for a in range(4)]
    for a in range(4):
        for b in range(4):
            for cc in range(4):
                tau = sp.simplify((psibar*(gam[a]*sigma_ab(b, cc) + sigma_ab(b, cc)*gam[a])*psi)[0])
                rest = {0, 1, 2, 3} - {a, b, cc}
                if len(rest) == 1:
                    dd = list(rest)[0]
                    expect = COEF*eps4(a, b, cc, dd)*K_lo[dd]
                else:
                    expect = 0
                if sp.simplify(tau - expect) != 0:
                    spin_ok = False
check("C2 Fierz identities J.K=0, J^2=-K^2, J^2=S^2+P^2 exact on 8 random rational spinors "
      "(T6.V Part D)", fierz_ok)
check("C3 Dirac spin tensor psibar{gamma^a,sigma^{bc}}psi is totally antisymmetric and equals "
      "COEF * eps^{abcd} K_d (spin source lives purely in the axial channel)", spin_ok)

# EC schematic elimination, exactly in T6's variables: L_T = alpha C_a C^a + beta C_a K^a.
al, be = sp.symbols('alpha beta')
Ca = sp.symbols('C0:4'); Ka = sp.symbols('K0:4')
Cup = [eta[a, a]*Ca[a] for a in range(4)]
Kup = [eta[a, a]*Ka[a] for a in range(4)]
LT = al*sum(Ca[a]*Cup[a] for a in range(4)) + be*sum(Ca[a]*Kup[a] for a in range(4))
eom = [sp.diff(LT, Ca[a]) for a in range(4)]
solC = sp.solve(eom, Ca, dict=True)[0]
check("C4 variation of L_T wrt C_a gives C_a = -beta/(2 alpha) K_a for every component (T6.V Part D)",
      all(sp.simplify(solC[Ca[a]] + be/(2*al)*Ka[a]) == 0 for a in range(4)))
LT_eff = sp.simplify(LT.subs(solC))
Ksq = sum(Ka[a]*Kup[a] for a in range(4))
check("C5 eliminating C_a gives L_T,eff = -beta^2/(4 alpha) K^2 exactly (T6.V Part D)",
      sp.simplify(LT_eff + be**2/(4*al)*Ksq) == 0)

# Part C arithmetic (T6.V): D_J = -(1/3) r^4 Omega'; L_rot -> p_Omega.
r, Om = sp.symbols('r Omega', positive=True)
Omp = sp.symbols("Omega'")
DJ = -sp.Rational(1, 3)*r**4*Omp
check("C6 on AN=1: r Omega'/4 = -3 D_J/(4 r^3) (T6.V Part C conversion)",
      sp.simplify(r*Omp/4 - (-3*DJ/(4*r**3))) == 0)
kap = sp.symbols('kappa_g', positive=True)
Lrot = -2*sp.pi/(3*kap)*r**4*Omp**2
pOm = sp.diff(Lrot, Omp)
check("C6b p_Omega = dL_rot/dOmega' = (4 pi / kappa_g) D_J (T6.V Part B)",
      sp.simplify(pOm - 4*sp.pi/kap*DJ) == 0)
G, Jm = sp.symbols('G J', positive=True)
Om_slow = 2*G*Jm/r**3
DJ_slow = sp.simplify(DJ.subs(Omp, sp.diff(Om_slow, r)))
pOm_slow = sp.simplify((4*sp.pi/kap*DJ).subs(Omp, sp.diff(Om_slow, r)).subs(kap, 8*sp.pi*G))
check("C6c slow-Kerr Omega=2GJ/r^3 gives D_J=2GJ and p_Omega=J at kappa_g=8 pi G",
      DJ_slow == 2*G*Jm and pOm_slow == Jm)
# Maxwell reduced action: no D_M dependence, cyclic momentum.
sg, Phi_p, gE, DM = sp.symbols('sigma Phi_p g_E D_M')
LEM = 2*sp.pi/gE**2*sp.exp(-sg)*r**2*Phi_p**2
check("C7 dL_EM^red/dD_M = 0 identically and p_Phi = (4 pi/g_E^2) e^{-sigma} r^2 Phi' (T6.V Part A)",
      sp.diff(LEM, DM) == 0 and sp.simplify(sp.diff(LEM, Phi_p)
      - 4*sp.pi/gE**2*sp.exp(-sg)*r**2*Phi_p) == 0)

npass = sum(1 for _, ok in results if ok)
print(f"\nSUMMARY: {npass}/{len(results)} checks PASS")
assert npass == len(results), "FAILURES PRESENT"
