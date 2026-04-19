# SEIR Models for Infectious Diseases

## Overview
This repository contains SEIR models for influenza and measles.
- S: Susceptible
- E: Exposed
- I: Infected
- R: Recovered

## Parameters
- β (beta): infection/transmission rate
- γ (gamma): recovery rate
- sigma: latent rate 

## For Measles
A school has 2,000 students
On a student returning from travel infected with measles
#Initial conditions, Infected people (I) = 1
#Initial condition, Exposed people (E) = 0
#Initial conditions, Recovered people (R) = 0
#Everyone is susceptible, SO

#infectious period = 8 days #realistic
#latent period = 8 days #realsitic for measles cases
#infection rate; beta(rate at which people move from suscpetible to infected) = 14/8
#recovery rate; gamma( rate at which infected people move to the recovery class = 1/8
#latent rate; sigma ( rate at which exposed people become infectious) = 1/8

## For Influenza
Population(N) : 10,000
Initial exposed people : 0
Initial infected (IO): 10
Initial recovered (RO_initial) : 0
Initial susceptible (SO): 9,990 (S0 = N - E0 - I0 - RO_initial) 
Transmission rate (beta): 3 / 10
Recovery rate (gamma): 1 / 5
latent rate (sigma) : 1 / 2


##R0 the basic reproduction number (how an infected person infects susceptible)
#When R < 1 = epidemic gradually reduces and dies out 
#when R > 1 = epidemic spread
#we plot Rt (effective reproduction number); which shows how RO increases with time 

## Equations
dSdt = -beta * S * I / N
dEdt = beta * S * I / N - sigma * E
dIdt = sigma * E - gamma * I
dRdt = gamma * I

## Files
influenza.py -- influenza simulation
measles.py -- measles simulation

## Interpretation
The model shows how diseases spread and stabilize over time depending on transmission, recovery rates and latent rates. 
