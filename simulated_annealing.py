import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import random

# Standard deviation for the transition kernel (controls step size of random moves)
sigma = 0.1

# Number of iterations for the simulated annealing algorithm
nb_iteration = 60000

# Cooling rate for temperature (controls how quickly the temperature decreases)
alpha = 0.7

# Initial temperature (higher temperature allows more exploration)
T = 40

def target_function(x):
    """
    Complex target function to optimize
    Includes multiple cosine terms and a linear term
    
    Components:
    - sin(5x)
    - Multiple cosine terms with different frequencies
    - Linear term x/10
    """
    return np.sin(5*x) + np.cos(3*x) + np.cos(x) + np.cos(2*x) + \
           np.cos(3*x) + np.cos(4*x) + np.cos(5*x) + x/10

def transition_kernel(x, y):
    """
    Probability density function for transitioning from x to y
    Uses a normal (Gaussian) distribution
    
    Args:
    - x: Current state
    - y: Proposed state
    
    Returns:
    - Transition probability
    """
    return norm.pdf(x, y, sigma)

def transition_kernel_random(x):
    """
    Generates a new proposed state using a normal distribution
    
    Args:
    - x: Current state
    
    Returns:
    - Proposed new state
    """
    return np.random.normal(x, sigma)

def ratio(x, y, T):
    """
    Compute the acceptance probability ratio
    
    Args:
    - x: Current state
    - y: Proposed state
    - T: Current temperature
    
    Returns:
    - Acceptance probability (capped at 1)
    """
    a = (np.exp(-target_function(x)/T) * transition_kernel(x, y)) / \
        (np.exp(-target_function(y)/T) * transition_kernel(y, x))
    return a if a < 1 else 1

# Initialize the starting point randomly from a normal distribution
x0 = np.random.normal(0, sigma)

# Simulated Annealing main loop
for i in range(nb_iteration):
    # Propose a new state
    x_next = transition_kernel_random(x0)
    
    # Compute acceptance probability
    b = ratio(x0, x_next, T)
    
    # Generate a random number to decide acceptance
    u = random.uniform(0, 1)
    
    # Accept or reject the proposed state
    if u <= b:
        x0 = x_next
    
    # Cool down the temperature
    T = alpha * T

# Prepare x values for plotting the entire function
x_values = np.linspace(-10, 10, 1000)

# Compute y values for the entire function
y_values = target_function(x_values)

# Use the last explored point as the optimum (this might not be the true global optimum)
x_optimum = x_next
y_optimum = target_function(x_optimum)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, 
         label=r'$f(x) = \sin(5x) + \cos(3x) + \sum_{i=1}^{5} \cos(i x) + \frac{x}{10}$', 
         color='b')

# Highlight the optimum point found by the algorithm
plt.scatter(x_optimum, y_optimum, color='red', s=100, 
            label=f'Optimum Point: ({x_optimum:.2f}, {y_optimum:.2f})')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Target Function with Optimum Point')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()