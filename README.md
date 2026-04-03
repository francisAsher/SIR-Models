# SIR Models for Infectious Diseases

## Overview
This repository contains SIR models for influenza and measles.

## Model Description
The SIR model divides the population into:
- S: Susceptible
- I: Infected
- R: Recovered

## Parameters
- β (beta): infection rate
- γ (gamma): recovery rate

## For Measles
# A school has 2,000 students
# On a student returning from travel infected with measles
#Initial conditions, Infected people (I) = 1
#Initial conditions, Recovered people (R) = 0
#Everyone is susceptible
#Let's choose beta(infection rate) = 1.8
# Also the recovery rate(gamma) = 0.2

## For Influenza
# Population(N) : 10,000
# Initial infected (IO): 10
# Initial recovered (RO_initial) : 0
# Initial susceptible (SO): 9,990
# Transmission rate (beta): 0.30
# Recovery rate (gamma): 0.20

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