# A school has 2,000 students
# On student returns from travel infected with measles
#Initial conditions, Infected people (I) = 1
#Initial conditions, Recovered people (R) = 0
#Everyone is susceptible
#Let's choose beta(infection rate) = 1.8
# Also the recovery rate(gamma) = 0.2

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N = 2000
IO = 1
EO = 0 #exposed people at the beginning
RO_initial = 0
SO = N - EO - IO - RO_initial

beta = 14 / 8
gamma = 1 / 8
sigma  = 1 / 8 #new latent rate

RO = beta / gamma
print('RO =', RO)

t = np.linspace(0, 60, 60)


def seir_model(y, t, N,  beta, gamma, sigma):
    S, E, I, R = y

    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma *  I

    return dSdt, dEdt, dIdt, dRdt

yO = SO, EO, IO, RO_initial

solution = odeint(seir_model, yO,  t, args = (N, beta, gamma, sigma))
S, E, I, R = solution.T


Rt = RO * (S / N)


plt.figure(figsize=(10, 6))

plt.plot(t, S, label='Susceptible')
plt.plot(t, E, label='Exposed', color= '#5d5078')
plt.plot(t, I, label='Infected')
plt.plot(t, R, label='Recovered')

plt.title('SEIR Model - Measles Spread In a School')
plt.xlabel('Days')
plt.ylabel('Population')
plt.legend()
plt.grid()

plt.show()


plt.figure(figsize=(10, 6))

plt.plot(t, Rt, label = 'Effective R (RT) ')
plt.axhline(y=1, linestyle = '--', label = 'Threshold (Rt=1)')

plt.title('Reproduction number')
plt.xlabel('Days')
plt.ylabel('Rt')

plt.legend()
plt.grid()
plt.show()


