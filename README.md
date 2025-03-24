# MONTE_CARLO_METHODS


This repository contains implementations of various Monte Carlo methods used for probabilistic sampling, optimization, and statistical inference. These methods are fundamental in computational mathematics, physics, and machine learning.

## Table of Contents
- [Overview](#overview)
- [Implemented Algorithms](#implemented-algorithms)
- [Usage](#usage)
- [References](#references)

## Overview
Monte Carlo methods are a class of algorithms that rely on repeated random sampling to obtain numerical results. They are widely used in simulations, statistical inference, and optimization problems.

## Implemented Algorithms
The following Monte Carlo methods are implemented in this repository:

1. **Box-Muller Algorithm (`box_muller_algorithm.py`)**  
   - Generates normally distributed random numbers using the Box-Muller transform.

2. **Hastings-Metropolis Algorithm (`hastings_metropolis_algorithm.py`)**  
   - A Markov Chain Monte Carlo (MCMC) method for obtaining a sequence of random samples from a probability distribution.

3. **Inverse Sampling Transform (`inverse_sampling_transform.py`)**  
   - A technique for generating random variables with a specified distribution using the inverse transform method.

4. **Reject Sampling Algorithm (`reject_sampling_algorithm.py`)**  
   - A method for generating samples from a probability distribution by rejecting certain candidates based on a criterion.

5. **Simulated Annealing (`simulated_annealing.py`)**  
   - A probabilistic optimization algorithm that mimics the annealing process in metallurgy to find a global minimum.

## Usage

Each script can be executed independently. Example usage:
```bash
python box_muller_algorithm.py 
```
## References
- [Monte Carlo Methods](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [Simulated Annealing Overview](https://en.wikipedia.org/wiki/Simulated_annealing)
- [Metropolis-Hastings Algorithm](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm)
- [Inverse Transform Sampling](https://en.wikipedia.org/wiki/Inverse_transform_sampling)
- [Box Muller Algorithm](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform)



Let me know if you want any tweaks! 🚀

