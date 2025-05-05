#!/usr/bin/env python3

import time
import math
import platform
from gpiozero import Motor, DistanceSensor, LightSensor, Button
from RPi.GPIO import setmode, BCM, setup, OUT, IN, output, input, cleanup
import smbus2

# Try to import Pi-top specific modules
try:
    from pitop import Pitop, UltrasonicSensor, ServoMotor, LightSensor as PiTopLightSensor, SoundSensor
    PITOP_AVAILABLE = True
except ImportError:
    PITOP_AVAILABLE = False

class AutonomousRobot:
    def __init__(self):
        # Initialize components based on platform
        if PITOP_AVAILABLE:
            self.robot = Pitop()
            self.ultrasonic = UltrasonicSensor("D0")
            self.servo = ServoMotor("S0")
            self.light_sensor = PiTopLightSensor("A0")
            self.sound_sensor = SoundSensor("A1")
        else:
            # Raspberry Pi GPIO setup
            setmode(BCM)
            # Define GPIO pins (adjust these numbers based on your wiring)
            self.MOTOR_LEFT_PINS = (17, 18)  # (forward, backward)
            self.MOTOR_RIGHT_PINS = (22, 23)
            self.ULTRASONIC_TRIG = 24
            self.ULTRASONIC_ECHO = 25
            self.LIGHT_SENSOR = 26
            self.SOUND_SENSOR = 27
            
            # Setup GPIO pins
            for pin in self.MOTOR_LEFT_PINS + self.MOTOR_RIGHT_PINS:
                setup(pin, OUT)
            setup(self.ULTRASONIC_TRIG, OUT)
            setup(self.ULTRASONIC_ECHO, IN)
            setup(self.LIGHT_SENSOR, IN)
            setup(self.SOUND_SENSOR, IN)
            
            # Initialize I2C for servo control
            self.bus = smbus2.SMBus(1)
            self.SERVO_ADDRESS = 0x40  # Adjust based on your servo controller
            
        # Movement parameters
        self.speed = 0.4
        self.turn_speed = 0.25
        self.safe_distance = 25
        self.scan_angle = 90
        self.target_light_level = 0.5
        
        if PITOP_AVAILABLE:
            self.servo.angle = 0
        
    def get_distance(self):
        """Get distance from ultrasonic sensor"""
        if PITOP_AVAILABLE:
            return self.ultrasonic.distance
        else:
            # Raspberry Pi ultrasonic sensor implementation
            output(self.ULTRASONIC_TRIG, True)
            time.sleep(0.00001)
            output(self.ULTRASONIC_TRIG, False)
            
            start_time = time.time()
            stop_time = time.time()
            
            while input(self.ULTRASONIC_ECHO) == 0:
                start_time = time.time()
                
            while input(self.ULTRASONIC_ECHO) == 1:
                stop_time = time.time()
                
            time_elapsed = stop_time - start_time
            distance = (time_elapsed * 34300) / 2  # Speed of sound in cm/s
            return distance
            
    def get_light_level(self):
        """Get light level from sensor"""
        if PITOP_AVAILABLE:
            return self.light_sensor.reading
        else:
            return input(self.LIGHT_SENSOR)
            
    def get_sound_level(self):
        """Get sound level from sensor"""
        if PITOP_AVAILABLE:
            return self.sound_sensor.reading
        else:
            return input(self.SOUND_SENSOR)
            
    def set_servo_angle(self, angle):
        """Set servo angle"""
        if PITOP_AVAILABLE:
            self.servo.angle = angle
        else:
            # Raspberry Pi servo control via I2C
            # Convert angle to PWM value (adjust based on your servo)
            pwm_value = int(angle * 2.5 + 150)  # Example conversion
            self.bus.write_byte_data(self.SERVO_ADDRESS, 0, pwm_value)
            
    def move_motor(self, left_speed, right_speed):
        """Control motors"""
        if PITOP_AVAILABLE:
            self.robot.left_motor.forward(left_speed)
            self.robot.right_motor.forward(right_speed)
        else:
            # Raspberry Pi motor control
            # Left motor
            if left_speed > 0:
                output(self.MOTOR_LEFT_PINS[0], True)
                output(self.MOTOR_LEFT_PINS[1], False)
            elif left_speed < 0:
                output(self.MOTOR_LEFT_PINS[0], False)
                output(self.MOTOR_LEFT_PINS[1], True)
            else:
                output(self.MOTOR_LEFT_PINS[0], False)
                output(self.MOTOR_LEFT_PINS[1], False)
                
            # Right motor
            if right_speed > 0:
                output(self.MOTOR_RIGHT_PINS[0], True)
                output(self.MOTOR_RIGHT_PINS[1], False)
            elif right_speed < 0:
                output(self.MOTOR_RIGHT_PINS[0], False)
                output(self.MOTOR_RIGHT_PINS[1], True)
            else:
                output(self.MOTOR_RIGHT_PINS[0], False)
                output(self.MOTOR_RIGHT_PINS[1], False)
                
    def stop(self):
        """Stop all motors"""
        if PITOP_AVAILABLE:
            self.robot.left_motor.stop()
            self.robot.right_motor.stop()
        else:
            self.move_motor(0, 0)
            
    def cleanup(self):
        """Cleanup GPIO pins"""
        if not PITOP_AVAILABLE:
            cleanup()
            
    def scan_environment(self):
        """Scan the environment for obstacles and light levels"""
        distances = []
        light_levels = []
        
        # Scan from -45 to 45 degrees
        for angle in range(-45, 46, 15):
            self.set_servo_angle(angle)
            time.sleep(0.1)
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
        
    def move_forward(self, duration=0.5):
        """Move forward for specified duration"""
        self.move_motor(self.speed, self.speed)
        time.sleep(duration)
        self.stop()
        
    def turn(self, angle):
        """Turn the robot by specified angle"""
        duration = abs(angle) / 90
        
        if angle > 0:
            self.move_motor(self.turn_speed, -self.turn_speed)
        else:
            self.move_motor(-self.turn_speed, self.turn_speed)
            
        time.sleep(duration)
        self.stop()
        
    def navigate(self):
        """Main navigation loop"""
        try:
            print("Starting autonomous navigation...")
            print("Press Ctrl+C to stop")
            
            while True:
                distances, light_levels = self.scan_environment()
                best_angle, best_score = self.find_best_direction(distances, light_levels)
                
                if self.get_sound_level() > 0.8:
                    print("Emergency stop: Loud sound detected!")
                    self.stop()
                    time.sleep(2)
                    continue
                    
                if best_score > 0.5:
                    self.move_forward()
                else:
                    self.turn(best_angle)
                    
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\nStopping robot...")
            self.stop()
            self.cleanup()
            print("Robot stopped successfully")

if __name__ == "__main__":
    robot = AutonomousRobot()
    robot.navigate() 