import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#N = 10000
##EO = 0
#IO = 10
#RO_initial = 0
#SO = N - EO - IO - RO_initial

##Distinguishing different age groups in the susceptible population
#0 - 4yrs
#5 - 49yrs
#50+ yrs

N1 = 2000 #0-4
N2 = 5000 #5-49
N3 = 3000 #50+

N = np.array([2000, 5000, 3000]) #populations(different age groups)

I1_O = 0
I2_o = 10 #infection starts in this age group
I3_O = 0

E1_O = E2_O = E3_O = 0 #Initial exposed conditions
R1_initial = R2_initial = R3_initial = 0 #Initial recovered conditions

#setting them as numpy arrays
EO = np.array([0, 0, 0])
IO = np.array([10, 0, 0])
R_initial = np.array([0, 0, 0])
SO = N - EO - IO - R_initial

#Contact Matrix -- number of contact within the age groups(where susceptible meets infectious)
#C = np.array([
#         [10, 5, 2],
#         [5, 8, 3],
#        [2, 2, 4]
#])

C = np.array([
         [10, 5, 2],
         [5, 8, 3],
         [2, 2, 4]
])


beta = 3 / 10
gamma = 1 / 5
sigma = 1 / 2

RO = beta / gamma
print('RO', RO)

t = np.linspace(start = 0, stop = 160, num = 400)


def seir_age_model(y, t, N, beta, gamma, sigma, C):
        S = y[0:3]
        E = y[3:6]
        I = y[6:9]
        R = y[9:12]

        lambda_ = beta * (C @ (I / N)) #force of infection (multiplying contact matrix through the infection vector)

        dSdt = -lambda_ * S
        dEdt = lambda_ * S - sigma * E
        dIdt = sigma * E - gamma * I
        dRdt = gamma * I

        return np.concatenate([dSdt, dEdt, dIdt, dRdt])

yO = np.concatenate([SO, EO, IO, R_initial])

solution = odeint(seir_age_model, yO, t,
                   args=(N, beta, gamma, sigma, C))

S = solution[:, 0:3]
E = solution[:, 3:6]
I = solution[:, 6:9]
R = solution[:, 9:12]


plt.plot(t, I[:,0], label='0–4')
plt.plot(t, I[:,1], label='5–49')
plt.plot(t, I[:,2], label='50+')
plt.legend()
plt.title('Influenza SEIR with Age Groups')
plt.xlabel('Days')
plt.ylabel('Infected')
plt.grid()
plt.show()






