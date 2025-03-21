## Arduino-Based Smart Vacuum Cleaner

## Project Overview
This project is an **Arduino-based Smart Vacuum Cleaner** that autonomously navigates and cleans surfaces. It uses **ultrasonic sensors** for obstacle detection, an **Arduino Uno** for control, and **DC motors** for movement. The vacuum cleaner is designed to work in both autonomous and remote-controlled modes via Bluetooth.

## Features
- **Autonomous Navigation** using sensors
- **Bluetooth Remote Control** support
- **Obstacle Avoidance**
- **Efficient Cleaning System**
- **Rechargeable Battery System**

## Components Used
- **Arduino Uno**
- **Motor Driver (L298N)**
- **DC Motors**
- **Ultrasonic Sensors**
- **Bluetooth Module (HC-05)**
- **Vacuum Suction Mechanism**
- **Rechargeable Battery Pack**

## Code Overview
The project includes **two versions** of the code:
1. **Arduino Code (C language)** - Controls the vacuum cleaner's motors based on sensor inputs and Bluetooth commands.
2. **Python Simulation Code** - A Python script that simulates the car's movement in **VS Code** when hardware is unavailable. Instead of actual motor movements, it prints messages to indicate direction changes.

## How to Run the Simulation Code (Python)
1. Install **Python 3.x**
2. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/smart-vacuum-cleaner.git
   ```
3. Navigate to the project folder:
   ```sh
   cd smart-vacuum-cleaner
   ```
4. Run the Python script:
   ```sh
   python simulation.py
   ```
5. Enter commands in the terminal:
   - `F` → Move Forward
   - `B` → Move Backward
   - `L` → Turn Left
   - `R` → Turn Right
   - `S` → Stop
   - `Q` → Quit Simulation

## Future Improvements
- Implement AI-based room mapping.
- Optimize power consumption.
- Integrate mobile app control.

## Contributing
Feel free to fork this repository, submit pull requests, or suggest improvements!

## License
This project is open-source and available to all the people who wants to work or improve code.

