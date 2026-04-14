import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N = 10000
IO = 10
RO_initial = 0
SO = N - IO - RO_initial

beta = 3 / 10
gamma = 1 / 5

RO = beta / gamma
print('RO', RO)

t = np.linspace(start = 0, stop = 160, num = 160)


def sir_model(y, t, N, beta, gamma):
        S, I, R = y

        dSdt = -beta * S * I / N
        dIdt = beta * I * S / N - gamma * I
        dRdt = gamma * I

        return dSdt, dIdt, dRdt

yO = SO, IO, RO_initial

solution = odeint(sir_model, yO, t, args=(N, beta, gamma))
S, I, R = solution.T

Rt = RO * (S / N)


plt.figure(figsize=(10,6))
plt.plot(t, S, label='Susceptible')
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





