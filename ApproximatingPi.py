# %%
import numpy as np, matplotlib.pyplot as plt

n = 10000 # points generated per batch
r_tot = 0
iterations = range(100000) # number of batches

# for plotting
k = 20
x_in, y_in, x_out, y_out = np.array([]), np.array([]), np.array([]), np.array([])

# compute in batches and add to r_tot
for i in iterations:
    x_values = np.random.uniform(0, 1, n)
    y_values = np.random.uniform(0, 1, n)

    distance = x_values**2 + y_values**2
    less_than_one = distance < 1

    # for plotting first k batches
    if i < k:
        x_in = np.append(x_in, x_values[less_than_one])
        y_in = np.append(y_in, y_values[less_than_one])
        x_out = np.append(x_out, x_values[~less_than_one])
        y_out = np.append(y_out, y_values[~less_than_one])
    
    r = np.sum(less_than_one)
    r_tot += r

total_points = n * len(iterations)

pi = (4 * r_tot) / total_points

percent_error = abs(((pi - np.pi) / np.pi) * 100)

print(f"Total points: {total_points:,}",
      f"Percent error: {percent_error}%",
      f"Actual Pi: {pi}",
      f"Theoretical Pi: {np.pi}", 
      sep='\n'
)

# graph for circle
theta = np.linspace(0, np.pi / 2, 100)
plt.plot(np.cos(theta), np.sin(theta), c='black', label='circle', alpha=.5)

# scatterplot of first k batches
plt.scatter(x_in, y_in, s=.5, c='r', label='inside', alpha=.1)
plt.scatter(x_out, y_out, s=.5, c='b', label='outside', alpha=.1)
plt.legend()
plt.title(f"Scatterplot for {n * k} points")
plt.show()
