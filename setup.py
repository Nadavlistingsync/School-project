from setuptools import setup, find_packages

setup(
    name="autonomous-robot",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pitop>=0.30.0",
        "numpy>=1.21.0",
        "opencv-python>=4.5.0",
        "gpiozero>=1.6.2",
        "pyserial>=3.5",
        "RPi.GPIO>=0.7.0",
        "smbus2>=0.4.1",
        "paramiko>=2.12.0"
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.10.0"
        ]
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Autonomous navigation system for Pi-top 4 robot",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/autonomous-robot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "robot-navigate=robot.autonomous_navigation:main",
            "robot-test=robot.tests.test_robot:main"
        ]
    }
) 