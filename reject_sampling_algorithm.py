import numpy as np
import matplotlib.pyplot as plt
import random

# Scaling constant for the instrumental distribution
C = 5

def instrumental_distribution():
    """
    Returns the value of the instrumental distribution.
    This is a uniform distribution with probability density 1/6.
    """
    return 1/6

def target_distribution(x):
    """
    Returns the value of the target distribution at point x.
    This is a complex distribution that combines exponential decay with
    oscillating sinusoidal components.
    """
    return np.exp((-x**2)/2)*((np.sin(6 + x))**2 + 3*((np.cos(x))**2)*(np.sin(4*x)**2)+1)

def acceptance(x):
    """
    Implements the acceptance-rejection test for point x.
    
    Generates a random height y between 0 and C*q(x), where q(x) is the instrumental distribution.
    Returns True if y is below the target distribution scaled by C*q(x).
    
    Args:
        x: The point to test for acceptance
        
    Returns:
        Boolean indicating whether the point should be accepted
    """
    y = random.uniform(0, C*instrumental_distribution())
    return y <= target_distribution(x)/C*instrumental_distribution()

# Generate 10,000 samples from the uniform distribution on [-3, 3]
list_uniform = [random.uniform(-3, 3) for _ in range(10000)]

# Initialize an empty list to store accepted samples
accepted_sample= []

# Apply rejection sampling: only keep points that pass the acceptance test
for x in list_uniform:
    if (acceptance(x)):
        accepted_sample.append(x)

# Generate x values for plotting the target distribution
x_values = np.linspace(-4, 4, 500)  # 500 points from -4 to 4
y_values = target_distribution(x_values)   

# Plot the histogram of accepted samples
plt.hist(accepted_sample, bins=30, density=True, alpha=0.6, color='b', label="Histogram of accepted_sample")

# Plot the normalized target distribution
# np.trapz computes the integral of y_values over x_values for normalization
plt.plot(x_values, y_values / np.trapz(y_values, x_values), 'r-', linewidth=2, label="Target Function (Normalized)")

# Add labels, legend, title, and grid
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.title("Histogram of Accepted Samples vs. Target Function")
plt.grid()

# Display the plot
plt.show()