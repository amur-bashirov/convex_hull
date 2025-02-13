import matplotlib.pyplot as plt
import numpy as np

# Load results
data = np.loadtxt("empirical_results.txt")
n_values, times = data[:, 0], data[:, 1]

# Compute theoretical O(n log n) curve
k = times[-1] / (n_values[-1] * np.log(n_values[-1]))  # Estimate constant k
theoretical_times = k * n_values * np.log(n_values)
plt.figure(figsize=(8, 6))
plt.plot(n_values, times, marker='o', linestyle='-', label="Measured Time")
plt.plot(n_values, theoretical_times, linestyle='--', label="O(n log n) Fit")
plt.xlabel("Number of Points (n)")
plt.ylabel("Execution Time (seconds)")
plt.xscale("log")
plt.yscale("log")
plt.title("Empirical vs. Theoretical Complexity")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(n_values, times, marker='o', linestyle='-', label="Measured Time")
plt.xlabel("Number of Points (n)")
plt.ylabel("Execution Time (seconds)")
plt.xscale("log")  # Use log scale for better visualization
plt.yscale("log")
plt.title("Convex Hull Empirical Analysis")
plt.legend()
plt.grid(True)
plt.show()
