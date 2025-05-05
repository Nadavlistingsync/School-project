#!/usr/bin/env python3

from pitop import (
    Camera,
    UltrasonicSensor,
    ServoMotor,
    LightSensor,
    SoundSensor,
    Pitop
)
import time

def test_components():
    print("Testing Pi-top components...")
    
    try:
        # Initialize Pi-top
        robot = Pitop()
        print("✓ Pi-top initialized successfully")
        
        # Test ultrasonic sensor
        try:
            ultrasonic = UltrasonicSensor("D0")
            distance = ultrasonic.distance
            print(f"✓ Ultrasonic sensor working (Distance: {distance:.2f} cm)")
        except Exception as e:
            print(f"✗ Ultrasonic sensor error: {str(e)}")
        
        # Test servo motor
        try:
            servo = ServoMotor("S0")
            servo.angle = 0
            time.sleep(1)
            servo.angle = 90
            print("✓ Servo motor working")
        except Exception as e:
            print(f"✗ Servo motor error: {str(e)}")
        
        # Test light sensor
        try:
            light = LightSensor("A0")
            reading = light.reading
            print(f"✓ Light sensor working (Reading: {reading:.2f})")
        except Exception as e:
            print(f"✗ Light sensor error: {str(e)}")
        
        # Test sound sensor
        try:
            sound = SoundSensor("A1")
            reading = sound.reading
            print(f"✓ Sound sensor working (Reading: {reading:.2f})")
        except Exception as e:
            print(f"✗ Sound sensor error: {str(e)}")
        
        # Test camera
        try:
            camera = Camera()
            camera.start_preview()
            time.sleep(2)
            camera.stop_preview()
            print("✓ Camera working")
        except Exception as e:
            print(f"✗ Camera error: {str(e)}")
            
    except Exception as e:
        print(f"Error initializing Pi-top: {str(e)}")
    
    print("\nComponent test complete!")

if __name__ == "__main__":
    test_components() 