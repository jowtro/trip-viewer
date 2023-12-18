import json
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import numpy as np
import numpy.ma as ma
from mplcursors import cursor
import plotly.graph_objects as go

# Your data (assuming it's stored in a list named 'events')
events = []

with open('mock_test.txt') as f:
    for line in f:
        event = json.loads(line)  # Use 'line' directly
        events.append(event)

# Extract relevant data for plotting
datetimes = [datetime.strptime(event["datetime"], "%Y-%m-%dT%H:%M:%S.000Z") for event in events]
engine_status = [event.get("engine", {"status": np.nan}).get("status", np.nan) for event in events]
# convert the engine status to a number if running = 1 if off = 0 else -1

# Create a mask for NaN values
nan_mask = [False if isinstance(status, (int, float)) else True for status in engine_status]

# Convert the list to a NumPy array and create a masked array
engine_status_array = np.array(engine_status)
masked_engine_status = ma.masked_array(engine_status_array, mask=nan_mask)

# Create subplots
fig, (ax3) = plt.subplots(1, sharex=True, figsize=(10, 8))

# Plot Gantt chart using scatter plot
ax3.scatter(datetimes, masked_engine_status, marker='o', color='blue', label='Engine_Status')
ax3.set_xlabel('Datetime')
ax3.set_ylabel('Engine_Status')
ax3.legend()

# Create and configure MPLCursors cursor
cursor(ax3)  # or just mplcursors.cursor()

# Formatting date axis
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
#ax3.xaxis.set_major_locator(mdates.SecondLocator(interval=10))  # Adjust interval as needed

# Rotate x-axis labels for better readability
plt.gcf().autofmt_xdate()

# Hide datetime legend
ax3.get_legend().set_visible(False)

# Show the plot
#plt.show()



# Plotly figure for Gantt chart
fig = go.Figure()

# Add Gantt chart using scatter plot
fig.add_trace(
    go.Scatter(
        x=datetimes,
        y=masked_engine_status,
        mode='markers',
        marker=dict(color='blue', size=8),
        name='Engine_Status'
    )
)

# Formatting layout
fig.update_layout(
    title='Engine Status Over Time',
    xaxis_title='Datetime',
    yaxis_title='Engine_Status',
    xaxis=dict(type='date'),
    showlegend=True,
)

# Show the plot
fig.show()