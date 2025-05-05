#!/usr/bin/env python3

import sys
from robot import AutonomousRobot

def test_robot():
    """Test basic robot functionality"""
    try:
        print("Initializing robot...")
        robot = AutonomousRobot()
        print("Robot initialized successfully!")
        
        print("\nTesting sensor readings:")
        print(f"Distance: {robot.get_distance()} cm")
        print(f"Light level: {robot.get_light_level()}")
        print(f"Sound level: {robot.get_sound_level()}")
        
        print("\nTesting servo movement...")
        for angle in [-45, 0, 45]:
            print(f"Setting servo angle to {angle} degrees")
            robot.set_servo_angle(angle)
            
        print("\nTesting motor control...")
        print("Moving forward for 1 second")
        robot.move_forward(1)
        
        print("\nTesting turn...")
        print("Turning 90 degrees")
        robot.turn(90)
        
        print("\nAll tests completed successfully!")
        
    except Exception as e:
        print(f"Error during testing: {str(e)}")
        return 1
        
    return 0

if __name__ == "__main__":
    sys.exit(test_robot()) 