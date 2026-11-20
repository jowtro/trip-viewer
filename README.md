# Description

## Data Visualization with Matplotlib

This Python script showcases a data visualization project that reads data from a log file, processes it, and then visualizes it using matplotlib.

### Step-by-Step Breakdown:

1. **Importing Libraries:**
   - `json`: Utilized for parsing JSON data.
   - `matplotlib.pyplot`: The primary plotting library within Matplotlib.
   - `datetime`: Offers tools for handling date and time data.
   - `matplotlib.dates`: Facilitates date handling within Matplotlib plots.
   - `numpy` and `numpy.ma`: Employed for numerical operations and handling masked arrays, respectively.

2. **Initializing Data Container:**
   - Creates an empty list `events` to store extracted data.

3. **Reading Log Data:**
   - Reads the file `mock_smallest.log` for data retrieval.
   - Iterates through each line, assuming it represents a JSON object.
   - Parses each JSON object and adds it to the `events` list.

4. **Extracting Data Chunks:**
   - Extracts the `datetime` and `engine_status` fields from each event.
   - Converts `datetime` to a Python `datetime` object for accurate processing.
   - Assigns a default value of `np.nan` (representing a missing value) for absent `engine_status`.

5. **Creating a Mask for Missing Values:**
   - Constructs a mask to identify missing values within the `engine_status` data.

6. **Processing Engine Status Data:**
   - Converts the `engine_status` list to a NumPy array.
   - Applies the mask to generate a masked array capable of handling missing data.

7. **Generating Data Plot:**
   - Establishes a subplot to display the data effectively.
   - Plots the `engine_status` against `datetime` using blue circles as data points.

8. **Adding Labels and Legend:**
   - Assigns labels to the x-axis (`datetime`) and y-axis (`engine_status`) for clarity.
   - Includes a legend to explain the plotted data.

## Installing and Running the Project

This project uses Poetry for dependency management. If you haven't installed it yet, you can do so by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

To install and run the project, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/username/project.git
    ```

2. Navigate to the project directory:
    ```
    cd project
    ```

3. Install the project dependencies:
    ```
    poetry install
    ```

4. Run the main script:
    ```
    poetry run python main.py
    ```

---

## Project Explanation

### Overview & Purpose
`trip-viewer` is a Python vehicle telemetry analysis and visualization toolkit managed with **Poetry**. It ingests newline-delimited JSON (JSON Lines) vehicle trip logs (`mock_test.txt`) containing high-frequency timestamped telemetry events (such as GPS coordinates, ignition/engine status, speed, and odometer readings), computes summary trip metrics with **Pandas**, and visualizes engine status timelines and data gaps using **Matplotlib**, **NumPy masked arrays (`numpy.ma`)**, and **mplcursors**.

### Architecture & Key Scripts

1. **Telemetry Dataset (`mock_test.txt`)**
   - Stores raw vehicle telemetry in JSON Lines (`.jsonl`) format where each line is a timestamped event payload containing nested objects such as `datetime` (`YYYY-MM-DDTHH:MM:SS.000Z`), `engine` (`{"status": "running" | "off"}`), `speed` (`{"value": ...}`), and `odometer` (`{"value": ...}`).

2. **Interactive Engine Status Timeline (`trip_chart.py`)**
   - Reads `mock_test.txt` line-by-line using `json.loads()`.
   - Parses ISO-8601 UTC timestamps into Python `datetime` objects (`datetime.strptime(..., "%Y-%m-%dT%H:%M:%S.000Z")`) and extracts `event["engine"]["status"]`, defaulting missing entries to `np.nan`.
   - Builds a boolean mask (`nan_mask`) and wraps the status series in a **NumPy Masked Array** (`numpy.ma.masked_array`) so missing telemetry points are cleanly omitted when plotting.
   - Renders a Matplotlib scatter/Gantt-style plot (`ax3.scatter`) formatted with `matplotlib.dates.DateFormatter('%Y-%m-%d %H:%M:%S')` and attaches interactive hover data cursors via `mplcursors.cursor(ax3)`.

3. **Pandas Trip Metrics Analyzer (`trip_analysis.py`)**
   - Loads `mock_test.txt` directly into a Pandas DataFrame via `pd.read_json('mock_test.txt', lines=True)`.
   - Computes key operational trip metrics from nested dictionary columns:
     - **Engine Running Time**: Count of telemetry records where `engine.status == 'running'`.
     - **Engine Off Time**: Count of telemetry records where `engine.status == 'off'`.
     - **Total Distance (`km`)**: Difference between the maximum and minimum `odometer.value` readings across the trip (`max() - min()`), safely handling missing `odometer` keys.
     - **Average Speed (`km/h`)**: Mean of all non-null `speed.value` entries (`dropna().mean()`).

4. **Matplotlib Experiments (`playground/`)**
   - `playground/gap_test.py`: Demonstrates how Matplotlib natively breaks line segments (`plt.plot`) when a numeric NumPy array (`speed`) contains `np.nan` values, creating visual gaps for missing telemetry intervals.
   - `playground/on_off.py`: Tests plotting categorical string arrays (`"running"`, `"off"`, `np.nan`) over time to observe how Matplotlib maps categorical states and `NaN` values on the Y-axis.
   - `playground/teste.py`: Minimal prototype demonstrating custom categorical tick label mapping using `ax.set_xticks()` and `ax.set_xticklabels()`.

### Running the Scripts

```bash
# Install dependencies via Poetry
poetry install

# Run the Pandas trip metrics summary
poetry run python trip_analysis.py

# Run the interactive Matplotlib engine status chart
poetry run python trip_chart.py

# Run the playground gap/categorical experiments
poetry run python playground/gap_test.py
poetry run python playground/on_off.py
```