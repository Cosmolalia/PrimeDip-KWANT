import os, numpy as np, sympy
from matplotlib import use
use('Agg')
import matplotlib.pyplot as plt

os.makedirs('sim_data', exist_ok=True)

L = 311
deltaE = 23.6
primes = list(sympy.primerange(2, 138))

energies = np.linspace(0, 500, 5000)
cond = np.ones_like(energies)

for p in primes:
    idx = np.argmin(np.abs(energies - p * deltaE))
    cond[idx] = 0.1
    for j in range(max(idx - 2, 0), min(idx + 3, len(energies))):
        cond[j] *= 0.5

plt.plot(energies, cond)
plt.xticks([p * deltaE for p in primes[::5]], labels=primes[::5], rotation=45)
plt.xlabel('Bias (mV)')
plt.ylabel('dI/dV (arb.)')
plt.title('Prime-Gap Dips')
plt.savefig('sim_data/prime_dip.png', dpi=300, bbox_inches='tight')
print('Plot saved to sim_data/prime_dip.png')
max_p = primes[-1]          # 137
max_e = max_p * deltaE      # 137 × 23.6 ≈ 3233 mV

energies = np.linspace(0, max_e, 10000)
cond = np.ones_like(energies)

for p in primes:
    idx = np.argmin(np.abs(energies - p * deltaE))
    cond[idx] = 0.1
    for j in range(max(idx-1,0), min(idx+2,len(energies))):
        cond[j] *= 0.3

plt.figure(figsize=(14,4))
plt.plot(energies, cond)
plt.xticks([p*deltaE for p in primes[::5]], labels=primes[::5], rotation=45)
plt.xlabel('Bias (mV)')
plt.ylabel('dI/dV (arb.)')
plt.title('All 33 Prime-Gap Dips')
plt.savefig('sim_data/prime_dip_full.png', dpi=300, bbox_inches='tight')
print('Full plot saved → sim_data/prime_dip_full.png')
