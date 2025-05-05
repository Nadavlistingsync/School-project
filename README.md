# Autonomous Navigation Robot

A Python-based autonomous navigation system for the Pi-top 4 robot, capable of navigating from one side of a room to another using various sensors and motors.

## Features

- Obstacle avoidance using ultrasonic sensors
- Light-based navigation
- Sound detection for emergency stops
- Smooth motor control
- Environment scanning and path planning

## Requirements

- Pi-top 4 or Raspberry Pi with compatible sensors
- Python 3.7+
- Required Python packages (see requirements.txt)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/autonomous-robot.git
cd autonomous-robot
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

## Usage

### Local Development

1. Run the test script to verify functionality:
```bash
python test_robot.py
```

2. Run the autonomous navigation system:
```bash
python -m robot.autonomous_navigation
```

### Remote Deployment

To deploy the project to a Raspberry Pi:

```bash
python -m robot.connect_to_pi <hostname> [username]
```

Example:
```bash
python -m robot.connect_to_pi 192.168.1.100 pi
```

## Project Structure

```
autonomous-robot/
├── src/
│   └── robot/
│       ├── __init__.py
│       ├── autonomous_navigation.py
│       ├── connect_to_pi.py
│       └── test_components.py
├── setup.py
├── requirements.txt
├── test_robot.py
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 