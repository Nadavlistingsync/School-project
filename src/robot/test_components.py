#!/usr/bin/env python3

from pitop import (
    Camera,
    UltrasonicSensor,
    ServoMotor,
    LightSensor,
    SoundSensor,
    Pitop,
    Battery
)
import time
from .config import *
from .logger import logger

def test_components():
    """Test all Pi-top 4 components"""
    logger.info("Starting Pi-top 4 component tests...")
    
    try:
        # Initialize Pi-top
        robot = Pitop()
        logger.info("✓ Pi-top initialized successfully")
        
        # Test battery
        try:
            battery = Battery()
            level = battery.percentage
            logger.info(f"✓ Battery working (Level: {level}%)")
        except Exception as e:
            logger.error(f"✗ Battery error: {str(e)}")
        
        # Test ultrasonic sensor
        try:
            ultrasonic = UltrasonicSensor(ULTRASONIC_PORT)
            distance = ultrasonic.distance
            logger.info(f"✓ Ultrasonic sensor working (Distance: {distance:.2f} cm)")
        except Exception as e:
            logger.error(f"✗ Ultrasonic sensor error: {str(e)}")
        
        # Test servo motor
        try:
            servo = ServoMotor(SERVO_PORT)
            servo.angle = 0
            time.sleep(1)
            servo.angle = 90
            time.sleep(1)
            servo.angle = 0
            logger.info("✓ Servo motor working")
        except Exception as e:
            logger.error(f"✗ Servo motor error: {str(e)}")
        
        # Test light sensor
        try:
            light = LightSensor(LIGHT_SENSOR_PORT)
            reading = light.reading
            logger.info(f"✓ Light sensor working (Reading: {reading:.2f})")
        except Exception as e:
            logger.error(f"✗ Light sensor error: {str(e)}")
        
        # Test sound sensor
        try:
            sound = SoundSensor(SOUND_SENSOR_PORT)
            reading = sound.reading
            logger.info(f"✓ Sound sensor working (Reading: {reading:.2f})")
        except Exception as e:
            logger.error(f"✗ Sound sensor error: {str(e)}")
        
        # Test camera
        try:
            camera = Camera(resolution=CAMERA_RESOLUTION, framerate=CAMERA_FRAMERATE)
            camera.start_preview()
            time.sleep(2)
            camera.stop_preview()
            logger.info("✓ Camera working")
        except Exception as e:
            logger.error(f"✗ Camera error: {str(e)}")
            
        # Test display
        try:
            robot.display.brightness = DISPLAY_BRIGHTNESS
            robot.display.timeout = DISPLAY_TIMEOUT
            logger.info("✓ Display working")
        except Exception as e:
            logger.error(f"✗ Display error: {str(e)}")
            
        # Test motors
        try:
            robot.left_motor.forward(0.5)
            robot.right_motor.forward(0.5)
            time.sleep(1)
            robot.left_motor.stop()
            robot.right_motor.stop()
            logger.info("✓ Motors working")
        except Exception as e:
            logger.error(f"✗ Motors error: {str(e)}")
            
    except Exception as e:
        logger.error(f"Error initializing Pi-top: {str(e)}")
        return False
    
    logger.info("Component test complete!")
    return True

if __name__ == "__main__":
    test_components() 