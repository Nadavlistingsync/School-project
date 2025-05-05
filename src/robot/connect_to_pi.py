#!/usr/bin/env python3

import paramiko
import os
import sys
from getpass import getpass

def connect_to_raspberry_pi(hostname, username, password=None):
    """
    Connect to Raspberry Pi using SSH and deploy the project
    """
    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # If password not provided, prompt for it
        if password is None:
            password = getpass(f"Enter password for {username}@{hostname}: ")
        
        # Connect to Raspberry Pi
        print(f"Connecting to {username}@{hostname}...")
        ssh.connect(hostname, username=username, password=password)
        
        # Create project directory
        print("Creating project directory...")
        stdin, stdout, stderr = ssh.exec_command('mkdir -p ~/autonomous-robot')
        
        # Setup virtual environment
        print("Setting up Python virtual environment...")
        commands = [
            'cd ~/autonomous-robot',
            'python3 -m venv venv',
            'source venv/bin/activate',
            'pip install --upgrade pip',
            'pip install -r requirements.txt'
        ]
        
        for cmd in commands:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            print(stdout.read().decode())
            if stderr.read():
                print(f"Error: {stderr.read().decode()}", file=sys.stderr)
        
        print("\nConnection successful! Project setup complete.")
        print("You can now run the autonomous navigation system with:")
        print("cd ~/autonomous-robot")
        print("source venv/bin/activate")
        print("python autonomous_navigation.py")
        
        ssh.close()
        
    except Exception as e:
        print(f"Error connecting to Raspberry Pi: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python connect_to_pi.py <hostname> [username]")
        sys.exit(1)
    
    hostname = sys.argv[1]
    username = sys.argv[2] if len(sys.argv) > 2 else "pi"
    
    connect_to_raspberry_pi(hostname, username) 