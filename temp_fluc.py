import statistics

def analyze_temperatures(temps):
    if not temps:
        raise ValueError("Temperature list is empty; cannot compute statistics.")

    n = len(temps)
    mean_val = statistics.mean(temps)
    median_val = statistics.median(temps)

    #  variance and stdev, need n ≥ 2; otherwise define as 0.0
    if n > 1:
        var_val = statistics.variance(temps)        # divides by (n-1)
        std_dev_val = statistics.stdev(temps)       # sqrt of sample variance
    else:
        var_val = 0.0
        std_dev_val = 0.0

    return {
        "mean": mean_val,
        "median": median_val,
        "variance": var_val,
        "standard_deviation": std_dev_val
    }

# Example usage
if __name__ == "__main__":
    datasets = [
        [],                    # empty
        [15.2],                # single reading
        [12.0, 15.5, 14.3, 13.8, 16.1]
    ]

    for temps in datasets:
        print(f"\nData: {temps}")
        try:
            stats = analyze_temperatures(temps)
            print(f"Mean:               {stats['mean']:.2f}")
            print(f"Median:             {stats['median']:.2f}")
            print(f"Sample Variance:    {stats['variance']:.4f}")
            print(f"Sample Std Deviation:{stats['standard_deviation']:.4f}")
        except ValueError as e:
            print("Error:", e)
