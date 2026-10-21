#!/usr/bin/env python3
"""T6 audit checks, part 3: spin-saturated pair cancellation (claim (d), T6.VI.N1).

Spinor (T6.I.4, kappa = -1, 1s_1/2): psi_m = ( F * Omega_{-1,m} , iG * Omega_{+1,m} )
with Omega the spinor spherical harmonics, built from exact Clebsch-Gordan
coefficients (sympy CG) and explicit Y_lm (cross-checked against sympy Ylm).
The common prefactor e^{-iEt}/(r sqrt(N)) of T6.I.4 is an overall positive
factor 1/(r^2 N) in all bilinears and is suppressed.
Currents are tetrad components: J^a = psibar gamma^a psi, K^a = psibar gamma^a gamma_5 psi.
Claim (T6.VI.2): J_pair proportional to (F^2+G^2, 0, 0, 0) and K_pair = 0.
Checks are exact (SymPy). Exit 0 iff all checks pass.
"""
import sympy as sp
from sympy.physics.quantum.cg import CG

results = []
def check(name, cond):
    results.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)

th, ph = sp.symbols('theta phi', real=True)
F, G = sp.symbols('F G', real=True)

# --- gamma matrices (Dirac rep, +---), as in part 1 ---
I2 = sp.eye(2); Z2 = sp.zeros(2)
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
def blk(a, b, c, d): return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))
gam = [blk(I2, Z2, Z2, -I2), blk(Z2, s1, -s1, Z2), blk(Z2, s2, -s2, Z2), blk(Z2, s3, -s3, Z2)]
g5 = sp.simplify(sp.I*gam[0]*gam[1]*gam[2]*gam[3])

# --- spherical harmonics (standard Condon-Shortley forms) ---
Y = {(0, 0): 1/(2*sp.sqrt(sp.pi)),
     (1, 0): sp.sqrt(3/sp.pi)*sp.cos(th)/2,
     (1, 1): -sp.sqrt(3/(2*sp.pi))*sp.sin(th)*sp.exp(sp.I*ph)/2,
     (1, -1): sp.sqrt(3/(2*sp.pi))*sp.sin(th)*sp.exp(-sp.I*ph)/2}
from sympy.functions.special.spherical_harmonics import Ynm as Ylm
okY = True
for (l, m), expr in Y.items():
    for tv, pv in [(sp.Rational(7, 10), sp.Rational(13, 10)), (sp.Rational(23, 10), sp.Rational(31, 10))]:
        ref = complex(Ylm(l, m, th, ph).subs({th: tv, ph: pv}).evalf())
        mine = complex(expr.subs({th: tv, ph: pv}).evalf())
        if abs(ref - mine) > 1e-12: okY = False
check("P0 explicit Y_lm forms agree with sympy Ylm numerically (1e-12) at sample points", okY)

def cg(l, ml, s, j, m):
    return sp.nsimplify(CG(l, ml, sp.Rational(1, 2), s, j, m).doit(), [sp.sqrt(2), sp.sqrt(3)])

def Omega(kappa, m):
    """Spinor spherical harmonic: l = j -/+ 1/2 for kappa = -/+1, j = 1/2."""
    l = 0 if kappa == -1 else 1
    comps = []
    for s in [sp.Rational(1, 2), sp.Rational(-1, 2)]:
        ml = m - s
        if abs(ml) > l:
            comps.append(sp.Integer(0))
            continue
        c = cg(l, ml, s, sp.Rational(1, 2), m)
        comps.append(sp.simplify(c*Y[(l, int(ml))]))
    return sp.Matrix(comps)

def currents(m):
    up = Omega(-1, m); lo = Omega(1, m)
    psi = sp.Matrix([F*up[0], F*up[1], sp.I*G*lo[0], sp.I*G*lo[1]])
    psibar = psi.conjugate().T*gam[0]
    J = [sp.simplify((psibar*gam[a]*psi)[0]) for a in range(4)]
    K = [sp.simplify((psibar*gam[a]*g5*psi)[0]) for a in range(4)]
    return J, K, up, lo

def zero(e):
    return sp.simplify(sp.trigsimp(sp.expand(e))) == 0

mp = sp.Rational(1, 2); mm = sp.Rational(-1, 2)
Jp, Kp, upp, lop = currents(mp)
Jm, Km, upm, lom = currents(mm)

check("P1 pointwise norms |Omega_-1,m|^2 = |Omega_+1,m|^2 = 1/(4 pi) for both m",
      all(zero(sp.simplify((Om.conjugate().T*Om)[0] - 1/(4*sp.pi))) for Om in (upp, lop, upm, lom)))
Jpair = [sp.simplify(Jp[a] + Jm[a]) for a in range(4)]
Kpair = [sp.simplify(Kp[a] + Km[a]) for a in range(4)]
check("P2 J_pair = ((F^2+G^2)/(2 pi), 0, 0, 0) pointwise (T6.VI.2)",
      zero(Jpair[0] - (F**2 + G**2)/(2*sp.pi)) and all(zero(Jpair[a]) for a in (1, 2, 3)))
check("P3 K_pair = (0,0,0,0) pointwise: exact axial-current cancellation (T6.VI.N1)",
      all(zero(Kpair[a]) for a in range(4)))
single_nonzero = any(not zero(Kp[a]) for a in range(4))
check("P4 control: single-m axial current K_{+1/2} is NOT identically zero "
      "(the pair cancellation is a real pair effect, not a triviality)", single_nonzero)
print("   K_{+1/2} components:", [sp.simplify(Kp[a]) for a in range(4)])
print("   K_{-1/2} components:", [sp.simplify(Km[a]) for a in range(4)])
print("   J_{+1/2} spatial:", [sp.simplify(Jp[a]) for a in (1, 2, 3)])

npass = sum(1 for _, ok in results if ok)
print(f"\nSUMMARY: {npass}/{len(results)} checks PASS")
assert npass == len(results), "FAILURES PRESENT"
