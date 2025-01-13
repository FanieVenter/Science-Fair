# Science Fair Project

Welcome to the repository for my Year 9 Science Fair project. This project involves data collection using an Arduino and data visualization with Python.

## Project Overview

The goal of this project is to collect environmental data using sensors connected to an Arduino microcontroller and visualize the collected data using Python. The project consists of two main components:

1. **Data Collection**: Utilizing an Arduino to gather data from various sensors.
2. **Data Visualization**: Employing Python to process and graph the collected data.

## Repository Contents

- `arduin_program.ino`: Arduino sketch for data collection.
- `grapher.py`: Python script for data visualization.
- `results/`: Directory containing collected data samples.

## Getting Started

To replicate this project, follow these steps:

1. **Arduino Setup**:
   - Connect the necessary sensors to the Arduino.
   - Upload the `arduin_program.ino` sketch to the Arduino using the Arduino IDE.

2. **Data Collection**:
   - Run the Arduino to collect data.
   - Save the collected data into the `results/` directory.

3. **Data Visualization**:
   - Ensure Python is installed on your system.
   - Install required Python libraries (e.g., `matplotlib`, `pandas`) using pip:
     ```bash
     pip install matplotlib pandas
     ```
   - Execute the `grapher.py` script to generate graphs from the collected data.

## Requirements

- **Hardware**:
  - Arduino microcontroller
  - Sensors (e.g., temperature, humidity)

- **Software**:
  - Arduino IDE
  - Python 3.x
  - Python libraries: `matplotlib`, `pandas`

## Usage

1. Collect data using the Arduino and save it in the `results/` directory.
2. Run the `grapher.py` script to visualize the data:
   ```bash
   python grapher.py
   ```
3. View the generated graphs to analyze the data.

## Contributing

This project is a personal educational endeavor. However, suggestions and improvements are welcome. Feel free to fork the repository and submit pull requests.

## License

This project is open-source and available under the [MIT License](LICENSE).

