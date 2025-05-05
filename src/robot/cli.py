#!/usr/bin/env python3

import argparse
from .autonomous_navigation import AutonomousRobot
from .logger import logger

def main():
    """Main entry point for the robot CLI."""
    parser = argparse.ArgumentParser(description='Autonomous Robot Control')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Navigation command
    nav_parser = subparsers.add_parser('navigate', help='Start autonomous navigation')
    nav_parser.add_argument('--speed', type=float, help='Movement speed')
    nav_parser.add_argument('--safe-distance', type=float, help='Safe distance from obstacles (cm)')
    
    # Test command
    test_parser = subparsers.add_parser('test', help='Run robot tests')
    test_parser.add_argument('--component', choices=['sensors', 'motors', 'all'], 
                           default='all', help='Component to test')
    
    args = parser.parse_args()
    
    if args.command == 'navigate':
        robot = AutonomousRobot()
        if args.speed:
            robot.speed = args.speed
        if args.safe_distance:
            robot.safe_distance = args.safe_distance
        logger.info("Starting autonomous navigation")
        robot.navigate()
        
    elif args.command == 'test':
        robot = AutonomousRobot()
        if args.component in ['sensors', 'all']:
            logger.info("Testing sensors...")
            print(f"Distance: {robot.get_distance()} cm")
            print(f"Light level: {robot.get_light_level()}")
            print(f"Sound level: {robot.get_sound_level()}")
            
        if args.component in ['motors', 'all']:
            logger.info("Testing motors...")
            robot.move_forward(1)
            robot.turn(90)
            robot.stop()
            
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 