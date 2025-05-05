"""
Configuration settings for the autonomous robot optimized for Pi-top 4.
"""

# Movement parameters
SPEED = 0.4
TURN_SPEED = 0.25
SAFE_DISTANCE = 25  # cm
SCAN_ANGLE = 90  # degrees
TARGET_LIGHT_LEVEL = 0.5

# Pi-top 4 specific pin configuration
ULTRASONIC_PORT = "D0"  # Port for ultrasonic sensor
SERVO_PORT = "S0"      # Port for servo motor
LIGHT_SENSOR_PORT = "A0"  # Port for light sensor
SOUND_SENSOR_PORT = "A1"  # Port for sound sensor

# Camera settings (Pi-top 4 specific)
CAMERA_RESOLUTION = (640, 480)
CAMERA_FRAMERATE = 30

# Emergency stop parameters
SOUND_THRESHOLD = 0.8  # Sound level threshold for emergency stop
EMERGENCY_STOP_DURATION = 2  # seconds

# Navigation parameters
SCAN_INTERVAL = 0.1  # seconds
MOVE_DURATION = 0.5  # seconds
TURN_DURATION = 1.0  # seconds

# Battery monitoring (Pi-top 4 specific)
BATTERY_WARNING_LEVEL = 20  # percentage
BATTERY_CRITICAL_LEVEL = 10  # percentage

# Display settings (Pi-top 4 specific)
DISPLAY_BRIGHTNESS = 100  # percentage
DISPLAY_TIMEOUT = 300  # seconds 