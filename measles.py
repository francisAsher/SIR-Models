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
RO_initial = 0
SO = N - IO - RO_initial

beta = 2.14
gamma = 0.143

RO = beta / gamma
print('RO =', RO)

t = np.linspace(0, 60, 60)


def sir_model(y, t, N,  beta, gamma):
    S, I, R = y

    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma *  I

    return dSdt, dIdt, dRdt

yO = SO, IO, RO_initial

solution = odeint(sir_model, yO,  t, args = (N, beta, gamma))
S, I, R = solution.T

#We can't plot RO on the SIR because it is constant, for SIR we need conditions which change with time
#we plot Rt instead, which is the Effective reproduction number
Rt = RO * (S / N)


plt.figure(figsize=(10, 6))

plt.plot(t, S, label='Susceptible')
plt.plot(t, I, label='Infected')
plt.plot(t, R, label='Recovered')

plt.title('Measles Spread In a School')
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


