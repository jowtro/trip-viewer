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