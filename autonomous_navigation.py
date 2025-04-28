#!/usr/bin/env python3

from pitop import Pitop
from pitop import UltrasonicSensor
from pitop import ServoMotor
from pitop import LightSensor
from pitop import SoundSensor
import time
import math

class PiTopAutonomousRobot:
    def __init__(self):
        # Initialize Pi-top 4 components
        self.robot = Pitop()
        self.ultrasonic = UltrasonicSensor("D0")
        self.servo = ServoMotor("S0")
        self.light_sensor = LightSensor("A0")
        self.sound_sensor = SoundSensor("A1")
        
        # Movement parameters
        self.speed = 0.4  # Reduced base speed for better control
        self.turn_speed = 0.25  # Reduced turn speed
        self.safe_distance = 25  # Minimum safe distance in cm
        self.scan_angle = 90  # Scanning angle for obstacle detection
        self.target_light_level = 0.5  # Target light level for navigation
        
        # Initialize servo to center position
        self.servo.angle = 0
        
    def scan_environment(self):
        """Scan the environment for obstacles and light levels"""
        distances = []
        light_levels = []
        
        # Scan from -45 to 45 degrees
        for angle in range(-45, 46, 15):
            self.servo.angle = angle
            time.sleep(0.1)  # Wait for servo to move
            distance = self.ultrasonic.distance
            light_level = self.light_sensor.reading
            distances.append((angle, distance))
            light_levels.append((angle, light_level))
            
        return distances, light_levels
    
    def find_best_direction(self, distances, light_levels):
        """Find the best direction to move based on obstacle distances and light levels"""
        # Combine distance and light level data
        combined_scores = []
        for (angle, distance), (_, light) in zip(distances, light_levels):
            # Score based on both distance and light level
            distance_score = min(distance / self.safe_distance, 1.0)
            light_score = abs(light - self.target_light_level)
            combined_score = distance_score * (1 - light_score)
            combined_scores.append((angle, combined_score))
            
        # Find the direction with the best combined score
        best_angle, best_score = max(combined_scores, key=lambda x: x[1])
        return best_angle, best_score
    
    def move_forward(self, duration=0.5):
        """Move forward for specified duration with smooth acceleration"""
        # Smooth acceleration
        for speed in [0.2, 0.4, self.speed]:
            self.robot.left_motor.forward(speed)
            self.robot.right_motor.forward(speed)
            time.sleep(0.1)
        
        time.sleep(duration)
        self.stop()
    
    def turn(self, angle):
        """Turn the robot by specified angle with smooth motion"""
        # Convert angle to duration (rough estimation)
        duration = abs(angle) / 90  # 90 degrees takes about 1 second
        
        # Smooth turning
        if angle > 0:
            # Turn right
            for speed in [0.1, 0.2, self.turn_speed]:
                self.robot.left_motor.forward(speed)
                self.robot.right_motor.backward(speed)
                time.sleep(0.1)
        else:
            # Turn left
            for speed in [0.1, 0.2, self.turn_speed]:
                self.robot.left_motor.backward(speed)
                self.robot.right_motor.forward(speed)
                time.sleep(0.1)
                
        time.sleep(duration)
        self.stop()
    
    def stop(self):
        """Stop all motors with smooth deceleration"""
        # Smooth deceleration
        for speed in [self.speed, 0.2, 0]:
            self.robot.left_motor.forward(speed)
            self.robot.right_motor.forward(speed)
            time.sleep(0.1)
        self.robot.left_motor.stop()
        self.robot.right_motor.stop()
    
    def navigate(self):
        """Main navigation loop"""
        try:
            print("Starting autonomous navigation...")
            print("Press Ctrl+C to stop")
            
            while True:
                # Scan environment
                distances, light_levels = self.scan_environment()
                best_angle, best_score = self.find_best_direction(distances, light_levels)
                
                # Check for sound (emergency stop)
                if self.sound_sensor.reading > 0.8:  # Loud sound detected
                    print("Emergency stop: Loud sound detected!")
                    self.stop()
                    time.sleep(2)  # Wait for 2 seconds
                    continue
                
                # If path is clear and score is good, move forward
                if best_score > 0.5:
                    self.move_forward()
                else:
                    # Turn towards the best direction
                    self.turn(best_angle)
                
                time.sleep(0.1)  # Small delay between iterations
                
        except KeyboardInterrupt:
            print("\nStopping robot...")
            self.stop()
            print("Robot stopped successfully")

if __name__ == "__main__":
    robot = PiTopAutonomousRobot()
    robot.navigate() 