import matplotlib.pyplot as plt
import numpy as np

# Sample data
time = np.arange(0, 10, 1)
speed = np.array([20, 25, 30, np.nan, 35, 40, 45, 50, 55, 60])

# Plotting the chart with a gap
plt.plot(time, speed, marker='o')
plt.xlabel('Time')
plt.ylabel('Speed')
plt.title('Speed Over Time with Gap')
plt.show()