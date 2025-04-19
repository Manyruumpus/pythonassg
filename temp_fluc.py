import statistics as s 

def get_temp_stats(temp_readings):
    if len(temp_readings) == 0:
        raise ValueError("Whoops — can't analyze an empty list of temps.")

    count = len(temp_readings)
    
    # Grab the basic stats
    avg_temp = s.mean(temp_readings)
    mid_val = s.median(temp_readings)

    # if only one reading then direct ans 
    if count > 1:
        temp_variance = s.variance(temp_readings)  # using sample variance (n-1)
        std_dev = s.stdev(temp_readings)
    else:
        temp_variance = 0.0   # let default this
        std_dev = 0.0         

    return {
        "mean": avg_temp,
        "median": mid_val,
        "variance": temp_variance,
        "standard_deviation": std_dev
    }

# Quick testing below ,basic sanity check
if __name__ == "__main__":
    sample_datasets = [
        [],                      # empty case, should raise error
        [15.2],                  # single item — edge case for variance
        [12.0, 15.5, 14.3, 13.8, 16.1]  # normal dataset
    ]

    for readings in sample_datasets:
        print(f"\nProcessing temps: {readings}")
        try:
            result = get_temp_stats(readings)
            print(f"Average:           {result['mean']:.2f}")
            print(f"Median:            {result['median']:.2f}")
            print(f"Variance:          {result['variance']:.4f}")
            print(f"Std Deviation:     {result['standard_deviation']:.4f}")
        except ValueError as problem:
            print("Something went wrong:", problem)
