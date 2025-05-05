"""
Configuration settings for the autonomous robot.
"""

# Movement parameters
SPEED = 0.4
TURN_SPEED = 0.25
SAFE_DISTANCE = 25  # cm
SCAN_ANGLE = 90  # degrees
TARGET_LIGHT_LEVEL = 0.5

# GPIO pin configuration (for standard Raspberry Pi)
MOTOR_LEFT_PINS = (17, 18)  # (forward, backward)
MOTOR_RIGHT_PINS = (22, 23)
ULTRASONIC_TRIG = 24
ULTRASONIC_ECHO = 25
LIGHT_SENSOR = 26
SOUND_SENSOR = 27

# I2C configuration
SERVO_ADDRESS = 0x40
I2C_BUS = 1

# Emergency stop parameters
SOUND_THRESHOLD = 0.8  # Sound level threshold for emergency stop
EMERGENCY_STOP_DURATION = 2  # seconds

# Navigation parameters
SCAN_INTERVAL = 0.1  # seconds
MOVE_DURATION = 0.5  # seconds
TURN_DURATION = 1.0  # seconds 