import matplotlib.pyplot as plt
import numpy as np
# Create a sample data
x = ['Apple', 'Banana', 'Cherry']
y = [5, 1, 3]

# Plot the data
fig, ax = plt.subplots()
ax.plot(y)

# Set the X-axis tick labels to the values in the string array
ax.set_xticks(range(len(x)))
ax.set_xticklabels(x)

plt.show()