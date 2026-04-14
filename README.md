# SEIR Models for Infectious Diseases

## Overview
This repository contains SIR models for influenza and measles.

## Model Description
The SIR model divides the population into:
- S: Susceptible
- E: Exposed
- I: Infected
- R: Recovered

## Parameters
- β (beta): infection rate
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
Initial infected (IO): 10
Initial recovered (RO_initial) : 0
Initial susceptible (SO): 9,990
Transmission rate (beta): 0.30
Recovery rate (gamma): 0.20

##R0 the basic reproduction number (how an infected person infects other susceptible)
#When R < 1 = epidemic gradually reduces and dies out 
#when R > 1 = epidemic spread
#we plot Rt (effective reproduction number); which shows how RO increases with time 

## Equations
dS/dt = -βSI  
dI/dt = βSI - γI  
dR/dt = γI  

## Files
influenza.py → influenza simulation
measles.py → measles simulation

## Interpretation
The model shows how diseases spread and stabilize over time depending on transmission and recovery rates.
