import random
import numpy as np
import matplotlib.pyplot as plt
import math

# Define the Box-Muller transform function to generate normally distributed numbers
def normalDistribution(x, y):
    """
    Applies the Box-Muller transform to convert uniform random variables into normally distributed random variables.
    Args:
        x (float): A uniform random variable between 0 and 1.
        y (float): Another uniform random variable between 0 and 1.
    Returns:
        float: A normally distributed random variable.
    """
    return math.sqrt(-2 * np.log(x)) * math.cos(2 * math.pi * y)


# Print the purpose of the program
print("This program's goal is to implement the Box-Muller algorithm\n")

# Ask the user for the number of random numbers to generate
nb = input("How many numbers do you want to generate? ")
nb = int(nb)  # Convert the input to an integer

# Generate two lists of uniformly distributed random numbers between 0 and 1
list_uniform_1 = [random.uniform(0, 1) for _ in range(nb)]
list_uniform_2 = [random.uniform(0, 1) for _ in range(nb)]

# Apply the Box-Muller transform to generate a list of normally distributed numbers
list_normal = [normalDistribution(list_uniform_1[i], list_uniform_2[i]) for i in range(nb)]

# Create a figure with two subplots for visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Index-value plot: Plot the generated normal distribution values against their indices
ax1.plot(list_normal, 'b.', markersize=2)  # 'b.' means blue dots
ax1.set_title('Index-Value Plot')
ax1.set_xlabel('Index')
ax1.set_ylabel('Value')

# Histogram: Plot the distribution of the generated normal values
ax2.hist(list_normal, bins=30, color='green', alpha=0.7)  # 30 bins, green bars, and some transparency
ax2.set_title('Histogram')
ax2.set_xlabel('Value')
ax2.set_ylabel('Frequency')

# Adjust layout to prevent overlap and display the plots
plt.tight_layout()
plt.show()