import random
import numpy as np
import matplotlib.pyplot as plt

# Define the inverse CDF (quantile function) for an exponential distribution with rate 2
def inverse_cdf_Exponential(x):
    """
    Computes the inverse CDF (quantile function) for an exponential distribution with rate 2.
    Args:
        x (float): A uniform random variable between 0 and 1.
    Returns:
        float: A random variable following an exponential distribution with rate 2.
    """
    rate = 2  # Rate parameter for the exponential distribution
    return -np.log(1 - x) / rate  # Inverse CDF formula: -ln(1 - x) / rate


def main():
    """
    Main function to generate uniform random variables, transform them into exponential random variables,
    and visualize the results using scatter plots and histograms.
    """
    # Print the purpose of the program
    print("This program's goal is to implement the inverse sampling transform for an exponential law of rate 2\n")

    # Ask the user for the number of random numbers to generate
    nb = input("How many numbers do you want to generate? ")
    nb = int(nb)  # Convert the input to an integer

    # Generate a list of uniformly distributed random numbers between 0 and 1
    list_uniform = [random.uniform(0, 1) for _ in range(nb)]

    # Transform the uniform random variables into exponential random variables using the inverse CDF
    exponential_list = [inverse_cdf_Exponential(x) for x in list_uniform]

    # Create a 2x2 grid of subplots for visualization
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Scatter plot for uniform random variables
    axes[0, 0].scatter(range(nb), list_uniform, color='blue', alpha=0.6)
    axes[0, 0].set_title("Uniform Random Variables (Scatter Plot)")
    axes[0, 0].set_xlabel("Index")
    axes[0, 0].set_ylabel("Value")

    # Histogram for uniform random variables
    axes[0, 1].hist(list_uniform, bins=30, color='blue', alpha=0.6, edgecolor='black')
    axes[0, 1].set_title("Uniform Random Variables (Histogram)")
    axes[0, 1].set_xlabel("Value")
    axes[0, 1].set_ylabel("Frequency")

    # Scatter plot for exponential random variables
    axes[1, 0].scatter(range(nb), exponential_list, color='red', alpha=0.6)
    axes[1, 0].set_title("Exponential Random Variables (Scatter Plot)")
    axes[1, 0].set_xlabel("Index")
    axes[1, 0].set_ylabel("Value")

    # Histogram for exponential random variables
    axes[1, 1].hist(exponential_list, bins=30, color='red', alpha=0.6, edgecolor='black')
    axes[1, 1].set_title("Exponential Random Variables (Histogram)")
    axes[1, 1].set_xlabel("Value")
    axes[1, 1].set_ylabel("Frequency")

    # Adjust layout to prevent overlap and display the plots
    plt.tight_layout()
    plt.show()


# Entry point of the program
if __name__ == "__main__":
    main()