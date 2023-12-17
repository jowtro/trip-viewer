import matplotlib.pyplot as plt
import numpy as np

# Sample data
time = np.arange(0, 10, 1)
engine_status = np.array(["running", "running", "running", np.nan, "running", "running", "running", "running", "running", "off"])

# Plotting the chart with a gap
plt.plot(time, engine_status, marker='o')
plt.xlabel('Time')
plt.ylabel('engine_status')
plt.title('Engine_status Over Time with Gap')
plt.show()