# Autonomous Robot Navigation System

This project implements an autonomous navigation system for a robot using either Pi-top or standard Raspberry Pi hardware. The system uses various sensors (ultrasonic, light, sound) to navigate through an environment while avoiding obstacles.

## Features

- Platform-independent implementation (works with both Pi-top and standard Raspberry Pi)
- Obstacle avoidance using ultrasonic sensors
- Light-based navigation
- Sound detection for emergency stops
- Smooth motor control
- Environment scanning with servo-mounted sensors

## Hardware Requirements

### For Pi-top:
- Pi-top 4
- Pi-top Ultrasonic Sensor
- Pi-top Servo Motor
- Pi-top Light Sensor
- Pi-top Sound Sensor

### For Standard Raspberry Pi:
- Raspberry Pi (3B+ or 4 recommended)
- Ultrasonic Sensor (HC-SR04)
- Servo Motor
- Light Dependent Resistor (LDR)
- Sound Sensor
- Motor Driver (L298N recommended)
- 2 DC Motors

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/autonomous-robot.git
cd autonomous-robot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. For Raspberry Pi setup:
- Connect the sensors according to the GPIO pin configuration in `autonomous_navigation.py`
- Adjust the GPIO pin numbers in the code to match your wiring
- Set the correct I2C address for your servo controller

## Usage

Run the autonomous navigation system:
```bash
python autonomous_navigation.py
```

The robot will:
1. Scan the environment using the ultrasonic sensor
2. Detect light levels
3. Navigate while avoiding obstacles
4. Stop on detecting loud sounds
5. Clean up GPIO pins when stopped

## Configuration

You can adjust the following parameters in the code:
- `speed`: Base movement speed (default: 0.4)
- `turn_speed`: Turning speed (default: 0.25)
- `safe_distance`: Minimum safe distance from obstacles in cm (default: 25)
- `scan_angle`: Scanning angle for obstacle detection (default: 90)
- `target_light_level`: Target light level for navigation (default: 0.5)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 