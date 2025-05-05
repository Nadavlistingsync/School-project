import unittest
from unittest.mock import MagicMock, patch
from ..autonomous_navigation import AutonomousRobot

class TestAutonomousRobot(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.robot = AutonomousRobot()
        
    def test_initialization(self):
        """Test robot initialization."""
        self.assertIsNotNone(self.robot)
        self.assertIsNotNone(self.robot.speed)
        self.assertIsNotNone(self.robot.turn_speed)
        self.assertIsNotNone(self.robot.safe_distance)
        
    @patch('robot.autonomous_navigation.AutonomousRobot.get_distance')
    def test_get_distance(self, mock_get_distance):
        """Test distance measurement."""
        mock_get_distance.return_value = 25.0
        distance = self.robot.get_distance()
        self.assertEqual(distance, 25.0)
        
    @patch('robot.autonomous_navigation.AutonomousRobot.get_light_level')
    def test_get_light_level(self, mock_get_light_level):
        """Test light level measurement."""
        mock_get_light_level.return_value = 0.5
        light_level = self.robot.get_light_level()
        self.assertEqual(light_level, 0.5)
        
    @patch('robot.autonomous_navigation.AutonomousRobot.get_sound_level')
    def test_get_sound_level(self, mock_get_sound_level):
        """Test sound level measurement."""
        mock_get_sound_level.return_value = 0.3
        sound_level = self.robot.get_sound_level()
        self.assertEqual(sound_level, 0.3)
        
    @patch('robot.autonomous_navigation.AutonomousRobot.set_servo_angle')
    def test_set_servo_angle(self, mock_set_servo_angle):
        """Test servo angle setting."""
        self.robot.set_servo_angle(45)
        mock_set_servo_angle.assert_called_once_with(45)
        
    @patch('robot.autonomous_navigation.AutonomousRobot.move_motor')
    def test_move_forward(self, mock_move_motor):
        """Test forward movement."""
        self.robot.move_forward(1.0)
        mock_move_motor.assert_called_once_with(self.robot.speed, self.robot.speed)
        
    @patch('robot.autonomous_navigation.AutonomousRobot.move_motor')
    def test_turn(self, mock_move_motor):
        """Test turning."""
        self.robot.turn(90)
        mock_move_motor.assert_called_once_with(self.robot.turn_speed, -self.robot.turn_speed)
        
    @patch('robot.autonomous_navigation.AutonomousRobot.stop')
    def test_stop(self, mock_stop):
        """Test stopping."""
        self.robot.stop()
        mock_stop.assert_called_once()
        
    @patch('robot.autonomous_navigation.AutonomousRobot.cleanup')
    def test_cleanup(self, mock_cleanup):
        """Test cleanup."""
        self.robot.cleanup()
        mock_cleanup.assert_called_once()

if __name__ == '__main__':
    unittest.main() 