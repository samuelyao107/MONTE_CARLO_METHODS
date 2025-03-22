import random
import numpy as np
import matplotlib.pyplot as plt

# This program goals is to implement the inverse sampling transform for an exponential law of rate 2

def inverse_cdf_Exponential(x):
    rate = 2
    return - np.log(1-x) / rate # the inverse cdf of an exponential law of rate b is -ln(1- x)/b

def main():

    print("This program goals is to implement the inverse sampling transform for an exponential law of rate 2\n")
    
    nb = input("How many numbers do you want to generate? ")

    nb= int(nb)

    list_uniform = [random.uniform(0, 1) for _ in range(nb)]

    exponential_list = [inverse_cdf_Exponential(x) for x in list_uniform]

    # Create a 2x2 grid of subplots
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

    # Display the figure
    plt.tight_layout()
    plt.show()


if __name__=="__main__":
    main()        