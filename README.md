# Autonomous Navigation Robot

A Python-based autonomous navigation system for the Pi-top 4 robot, capable of navigating from one side of a room to another using various sensors and motors.

## Features

- Obstacle avoidance using ultrasonic sensors
- Light-based navigation
- Sound detection for emergency stops
- Smooth motor control
- Environment scanning and path planning
- Comprehensive logging system
- Command-line interface
- Unit tests and test coverage

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

4. Install test dependencies (optional):
```bash
pip install -e ".[test]"
```

## Usage

### Command Line Interface

The robot can be controlled using the command-line interface:

```bash
# Start autonomous navigation
python -m robot.cli navigate --speed 0.5 --safe-distance 30

# Test robot components
python -m robot.cli test --component sensors
python -m robot.cli test --component motors
python -m robot.cli test --component all
```

### Python API

You can also use the robot as a Python package:

```python
from robot import AutonomousRobot

# Create and initialize robot
robot = AutonomousRobot()

# Start autonomous navigation
robot.navigate()

# Or control manually
robot.move_forward(1.0)
robot.turn(90)
robot.stop()
```

### Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=robot
```

## Project Structure

```
autonomous-robot/
├── src/
│   └── robot/
│       ├── __init__.py
│       ├── autonomous_navigation.py
│       ├── connect_to_pi.py
│       ├── config.py
│       ├── logger.py
│       ├── cli.py
│       └── tests/
│           ├── __init__.py
│           └── test_robot.py
├── setup.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Configuration

The robot's behavior can be configured by modifying the settings in `src/robot/config.py`:

- Movement parameters (speed, turn speed, etc.)
- GPIO pin configuration
- I2C settings
- Emergency stop parameters
- Navigation parameters

## Logging

The robot includes a comprehensive logging system that writes to both console and file. Log files are created with timestamps in the format `robot_YYYYMMDD_HHMMSS.log`.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 