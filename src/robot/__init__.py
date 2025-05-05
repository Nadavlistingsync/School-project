"""
Autonomous Navigation Robot Package

This package provides the core functionality for autonomous robot navigation
using Pi-top 4 or standard Raspberry Pi hardware.
"""

from .autonomous_navigation import AutonomousRobot
from .connect_to_pi import connect_to_raspberry_pi

__version__ = '1.0.0'
__all__ = ['AutonomousRobot', 'connect_to_raspberry_pi'] 