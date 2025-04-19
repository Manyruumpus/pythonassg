import numpy as np
import matplotlib.pyplot as plt
import random

def set_seed(val):
    # Lock both numpy and random so results are consistent
    np.random.seed(val)
    random.seed(val)

def make_dataset(num_points, x_lo, x_hi):
    # Random X values
    x_vals = np.random.uniform(x_lo, x_hi, num_points)
    
    # Grab some random constants (used as scalars)
    A, B, C, D, E, F = np.random.uniform(0.5, 2.0, size=6)

    # Candidate functions (a bit of a grab bag)
    choices = [
        (np.sin, "sin"),
        (np.cos, "cos"),
        (np.tan, "tan"),
        (np.log, "log"),  # we should be careful with log(x) for x <= 0
        (lambda x: x**2, "square"),
        (lambda x: x**3, "cube")
    ]

    # Pick 3 different ones at random
    selected_funcs = random.sample(choices, 3)
    (f1, n1), (f2, n2), (f3, n3) = selected_funcs

    # Compute Y — messy but fun
    y_vals = A * f1(B * x_vals) + C * f2(D * x_vals) + E * f3(F * x_vals)

    # We'll print this so people know what function they’re seeing
    equation = (
        f"Y = {A:.2f}*{n1}({B:.2f}*X) + "
        f"{C:.2f}*{n2}({D:.2f}*X) + "
        f"{E:.2f}*{n3}({F:.2f}*X)"
    )

    return x_vals, y_vals, equation


def show_scatter(x, y):
    plt.figure()
    plt.scatter(x, y, alpha=0.75)
    plt.title("Scatter: X vs Y")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


def show_histogram(x):
    plt.figure()
    plt.hist(x, bins='auto', color='skyblue', edgecolor='black')
    plt.title("Histogram of X")
    plt.xlabel("X values")
    plt.ylabel("Count")
    plt.grid(True)
    plt.show()


def show_boxplot(y):
    plt.figure()
    plt.boxplot(y, vert=True)
    plt.title("Box Plot for Y")
    plt.ylabel("Y values")
    plt.grid(True)
    plt.show()


def show_lineplot(x, y):
    # Sort to get a smooth-ish line plot
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]

    plt.figure()
    plt.plot(x_sorted, y_sorted, linestyle='-', color='green')
    plt.title("Line Plot (Sorted X vs Y)")
    plt.xlabel("X (sorted)")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


def main():
    # Grab user inputs (could add validation later)
    seed = int(input("Random seed to use: "))
    N = int(input("How many data points? "))
    xmin = float(input("Lowest X value: "))
    xmax = float(input("Highest X value: "))

    # Lock seed for reproducibility
    set_seed(seed)

    # Build the dataset and display the chosen function
    X, Y, formula = make_dataset(N, xmin, xmax)
    print("\nGenerated Function:")
    print(formula)
    print()

    # Now show some plots
    show_scatter(X, Y)
    show_histogram(X)
    show_boxplot(Y)
    show_lineplot(X, Y)


# Run it
if __name__ == "__main__":
    main()
