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

## Equations
dS/dt = -βSI  
dI/dt = βSI - γI  
dR/dt = γI  

## Files
- sir_influenza.py → influenza simulation
- sir_measles.py → measles simulation

## Interpretation
The model shows how diseases spread and stabilize over time depending on transmission and recovery rates.