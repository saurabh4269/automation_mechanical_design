# Optimization, Automation in Mechanical Design

This project aims to streamline the design process of circular droplet separators by developing a mathematical model for efficient profile organization and creating scripts to automatically generate 3D models in Autodesk Inventor based on user inputs. This will simplify the creation of separators for any disk specification, saving time and effort.

### Approach

1. **Mathematical Modeling:**
   - Developed a mathematical model to optimize profile grouping using Python and scientific libraries.
   
2. **3D Modeling with Autodesk Inventor API:**
   - Utilized Autodesk Inventor's API to create scripts that generate 3D models based on user inputs.
   - Created a base script (`normal_method_temp.py`) for generating a cylinder with specified dimensions.
   
3. **GUI for User Input:**
   - Designed a simple GUI using Tkinter to take user inputs for the cylindrical segment dimensions and save path.
   - Developed `cylinder.py` to handle user inputs and create the 3D model using the Inventor API.
   
4. **Integration and Automation:**
   - Integrated the mathematical model with the 3D model generation script.
   - Automated the end-to-end process from user input to 3D model creation.

## Requirements

- Python 3.x
- Autodesk Inventor (with API access)
- Required Python packages (listed in `requirements.txt`)

## Setup Instructions

1. **Install Autodesk Inventor:**
   - Ensure Autodesk Inventor is installed on your Windows system and API access is set up.

2. **Install Python and Required Packages:**
   - Install Python 3.x from [Python.org](https://www.python.org/downloads/).
   - Install the required packages using the command:
     ```sh
     pip install -r requirements.txt
     ```

3. **Clone or Download the Repository:**
   - Clone this repository or download the ZIP file and extract it.

## Usage Instructions

### Running the Base Script

1. **Run `normal_method_temp.py`:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing `normal_method_temp.py`.
   - Run the script:
     ```sh
     python normal_method_temp.py
     ```
   - Enter the radius, height, and angle when prompted to create the cylindrical segment.

### Using the Pratical Library Script

1. **Run `cylinder.py`:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing `cylinder.py`.
   - Run the script:
     ```sh
     python cylinder.py
     ```
   - The GUI will open, allowing you to enter the radius, angle, and height for the cylinder.
   - Select the save directory for the generated 3D model.
   - Click "Submit" to generate the model.

## File Descriptions

- **`requirements.txt`**: Lists the required Python packages.
- **`normal_method_temp.py`**: Script to generate a cylindrical segment based on user input via the console.
- **`cylinder.py`**: GUI-based script to take user inputs and generate the 3D model using the Inventor API.
- **`inventor.py`**: Contains helper functions and classes for interacting with Autodesk Inventor.
