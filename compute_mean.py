import argparse
import numpy as np
from time import time
from generate import generate_random_points
from convex_hull import compute_hull

def measure_runtime(n, distribution, seed, num_trials=5):
    times = []
    for _ in range(num_trials):
        points = generate_random_points(distribution, n, seed)
        start = time()
        compute_hull(points)
        end = time()
        times.append(end - start)
    return times  # Compute the mean time over trials

if __name__ == '__main__':
    sizes = [10, 100, 1000, 10_000, 100_000, 500_000, 1_000_000]
    distribution = "normal"  # or "uniform"
    seed = 312

    results = []
    for n in sizes:
        times = measure_runtime(n, distribution, seed)
        mean_time = np.mean(times)
        results.append((n,times, mean_time))
        print(f"n = {n},Raw Times: {times},  Mean Time = {mean_time:.4f} seconds")

    # Save results to a file
    with open("empirical_results.txt", "w") as f:
        for n,T, t in results:
            f.write(f"n={n}, Raw Times: {T}, Mean Time = {t:.4f}\n")
