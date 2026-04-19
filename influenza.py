import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N = 10000
EO = 0
IO = 10
RO_initial = 0
SO = N - EO - IO - RO_initial

beta = 3 / 10
gamma = 1 / 5
sigma = 1 / 2

RO = beta / gamma
print('RO', RO)

t = np.linspace(start = 0, stop = 160, num = 160)


def seir_model(y, t, N, beta, gamma, sigma):
        S, E, I, R = y

        dSdt = -beta * S * I / N
        dEdt = beta * S * I / N - sigma * E
        dIdt = sigma * E - gamma * I
        dRdt = gamma * I

        return dSdt, dEdt, dIdt, dRdt

yO = SO, EO, IO, RO_initial

solution = odeint(seir_model, yO, t, args=(N, beta, gamma, sigma))
S, E, I, R = solution.T

Rt = RO * (S / N)


plt.figure(figsize=(10,6))
plt.title('SEIR Model for an Influenza Case')
plt.plot(t, S, label='Susceptible')
plt.plot(t, E, label='Exposed', color= '#5d5078')
plt.plot(t, I, label='Infected')
plt.plot(t, R, label='Recovered')
plt.xlabel('Days')
plt.ylabel('Population')
plt.grid()
plt.legend()
plt.show()


plt.figure(figsize=(10,6))
plt.plot(t, Rt, label='Effective R (Rt)')
plt.axhline(y = 1, color = 'red', linestyle = '--', label = 'Threshold (Rt=1')
plt.title('Effective Reproduction Number')
plt.xlabel('Days')
plt.ylabel('Rt')

plt.grid()
plt.legend()
plt.show()





