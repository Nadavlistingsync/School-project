#!/usr/bin/env python3

import time
import math
from pitop import Pitop, UltrasonicSensor, ServoMotor, LightSensor, SoundSensor, Camera, Battery
from .config import *
from .logger import logger

class AutonomousRobot:
    def __init__(self):
        """Initialize the robot with Pi-top 4 components"""
        self.robot = Pitop()
        self.ultrasonic = UltrasonicSensor(ULTRASONIC_PORT)
        self.servo = ServoMotor(SERVO_PORT)
        self.light_sensor = LightSensor(LIGHT_SENSOR_PORT)
        self.sound_sensor = SoundSensor(SOUND_SENSOR_PORT)
        self.camera = Camera(resolution=CAMERA_RESOLUTION, framerate=CAMERA_FRAMERATE)
        self.battery = Battery()
        
        # Movement parameters
        self.speed = SPEED
        self.turn_speed = TURN_SPEED
        self.safe_distance = SAFE_DISTANCE
        self.scan_angle = SCAN_ANGLE
        self.target_light_level = TARGET_LIGHT_LEVEL
        
        # Initialize servo
        self.servo.angle = 0
        
        # Setup display
        self.robot.display.brightness = DISPLAY_BRIGHTNESS
        self.robot.display.timeout = DISPLAY_TIMEOUT
        
        logger.info("Robot initialized successfully")
        
    def get_distance(self):
        """Get distance from ultrasonic sensor"""
        return self.ultrasonic.distance
            
    def get_light_level(self):
        """Get light level from sensor"""
        return self.light_sensor.reading
            
    def get_sound_level(self):
        """Get sound level from sensor"""
        return self.sound_sensor.reading
            
    def set_servo_angle(self, angle):
        """Set servo angle"""
        self.servo.angle = angle
            
    def move_motor(self, left_speed, right_speed):
        """Control motors"""
        self.robot.left_motor.forward(left_speed)
        self.robot.right_motor.forward(right_speed)
                
    def stop(self):
        """Stop all motors"""
        self.robot.left_motor.stop()
        self.robot.right_motor.stop()
            
    def check_battery(self):
        """Check battery level and log warnings if needed"""
        battery_level = self.battery.percentage
        if battery_level <= BATTERY_CRITICAL_LEVEL:
            logger.warning(f"Critical battery level: {battery_level}%")
            return False
        elif battery_level <= BATTERY_WARNING_LEVEL:
            logger.warning(f"Low battery level: {battery_level}%")
        return True
            
    def scan_environment(self):
        """Scan the environment for obstacles and light levels"""
        distances = []
        light_levels = []
        
        # Scan from -45 to 45 degrees
        for angle in range(-45, 46, 15):
            self.set_servo_angle(angle)
            time.sleep(SCAN_INTERVAL)
            distance = self.get_distance()
            light_level = self.get_light_level()
            distances.append((angle, distance))
            light_levels.append((angle, light_level))
            
        return distances, light_levels
        
    def find_best_direction(self, distances, light_levels):
        """Find the best direction to move based on obstacle distances and light levels"""
        combined_scores = []
        for (angle, distance), (_, light) in zip(distances, light_levels):
            distance_score = min(distance / self.safe_distance, 1.0)
            light_score = abs(light - self.target_light_level)
            combined_score = distance_score * (1 - light_score)
            combined_scores.append((angle, combined_score))
            
        best_angle, best_score = max(combined_scores, key=lambda x: x[1])
        return best_angle, best_score
        
    def move_forward(self, duration=MOVE_DURATION):
        """Move forward for specified duration"""
        self.move_motor(self.speed, self.speed)
        time.sleep(duration)
        self.stop()
        
    def turn(self, angle):
        """Turn the robot by specified angle"""
        duration = abs(angle) / 90 * TURN_DURATION
        
        if angle > 0:
            self.move_motor(self.turn_speed, -self.turn_speed)
        else:
            self.move_motor(-self.turn_speed, self.turn_speed)
            
        time.sleep(duration)
        self.stop()
        
    def navigate(self):
        """Main navigation loop"""
        try:
            logger.info("Starting autonomous navigation...")
            logger.info("Press Ctrl+C to stop")
            
            while True:
                if not self.check_battery():
                    logger.error("Critical battery level detected. Stopping navigation.")
                    break
                    
                distances, light_levels = self.scan_environment()
                best_angle, best_score = self.find_best_direction(distances, light_levels)
                
                if self.get_sound_level() > SOUND_THRESHOLD:
                    logger.warning("Emergency stop: Loud sound detected!")
                    self.stop()
                    time.sleep(EMERGENCY_STOP_DURATION)
                    continue
                    
                if best_score > 0.5:
                    self.move_forward()
                else:
                    self.turn(best_angle)
                    
                time.sleep(SCAN_INTERVAL)
                
        except KeyboardInterrupt:
            logger.info("Stopping robot...")
            self.stop()
            logger.info("Robot stopped successfully")
        except Exception as e:
            logger.error(f"Error during navigation: {str(e)}")
            self.stop()

if __name__ == "__main__":
    robot = AutonomousRobot()
    robot.navigate() 