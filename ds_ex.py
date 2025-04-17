import numpy as np
import matplotlib.pyplot as plt
import random

def set_random_seed(seed):
    np.random.seed(seed)
    random.seed(seed)

def generate_dataset(N, x_min, x_max):
    # Sample X
    X = np.random.uniform(x_min, x_max, N)
    
    # Random constants A, B, C, D, E, F
    A, B, C, D, E, F = np.random.uniform(0.5, 2.0, size=6)
    
    # Candidate functions
    funcs = [
        (np.sin,   "sin"),
        (np.cos,   "cos"),
        (np.tan,   "tan"),
        (np.log,   "log"),    # ensure x>0
        (lambda x: x**2, "square"),
        (lambda x: x**3, "cube")
    ]
    
    # Pick three distinct functions
    chosen = random.sample(funcs, 3)
    (f1, n1), (f2, n2), (f3, n3) = chosen
    
    # Compute Y
    Y = A * f1(B * X) + C * f2(D * X) + E * f3(F * X)
    
    # 6. Build a descriptive string
    func_str = (
        f"Y = {A:.2f}*{n1}({B:.2f}*X) + "
        f"{C:.2f}*{n2}({D:.2f}*X) + "
        f"{E:.2f}*{n3}({F:.2f}*X)"
    )
    return X, Y, func_str

def plot_scatter(X, Y):
    # Scatter plot of X vs Y
    plt.figure()
    plt.scatter(X, Y)
    plt.title("Scatter Plot of X vs Y")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

def plot_histogram(X):
    # Histogram of X
    plt.figure()
    plt.hist(X, bins='auto')
    plt.title("Histogram of X")
    plt.xlabel("X")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def plot_box(Y):
    # Box plot of Y
    plt.figure()
    plt.boxplot(Y, vert=True)
    plt.title("Box Plot of Y")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

def plot_line(X, Y):
    # Line plot of sorted X vs corresponding Y
    idx = np.argsort(X)
    Xs, Ys = X[idx], Y[idx]
    plt.figure()
    plt.plot(Xs, Ys)
    plt.title("Line Plot of Sorted X vs Y")
    plt.xlabel("X (sorted)")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

def main():
    # User inputs
    seed   = int(input("Enter random seed: "))
    N      = int(input("Enter number of data points (N): "))
    x_min  = float(input("Enter minimum X value: "))
    x_max  = float(input("Enter maximum X value: "))
    
    #  Set seed
    set_random_seed(seed)
    
    #  Generate dataset
    X, Y, func_str = generate_dataset(N, x_min, x_max)
    print("\nGenerated function:")
    print(func_str, "\n")
    
    #  Visualizations
    plot_scatter(X, Y)
    plot_histogram(X)
    plot_box(Y)
    plot_line(X, Y)

#  to run the code 
if __name__ == "__main__":
    main()
