# TurtleSim-Task
This project uses ROS2 and TurtleSim to draw various geometric shapes like squares, circles, and lines using a simulated turtle. The turtle moves and draws according to velocity commands,without direct teleporting.

Features
Move the turtle using velocity-based control.
Rotate the turtle by a specific angle.
Draw shapes such as squares, circles, and lines.
Lift and lower the pen to control drawing.

Installation

Prerequisites

Ubuntu 22.04 (or any ROS2-compatible Linux distro)

ROS2 Humble installed

Turtlesim package installed

sudo apt install ros-humble-turtlesim

Clone the Repository

https://github.com/TechTinkerKetki/TurtleSim-Task/
cd turtle_draw

Build the Package

The package should contain the following files:
1.package.xml 
2.setup.py
3.code.py

Running the Project

1.Launch turtlesim

2.ros2 run turtlesim turtlesim_node

Run the drawing node

1.ros2 run turtle-drawing draw_node

The turtle will now execute the predefined movements to draw the required shapes.

Code Structure

Main Execution (main.py)- calls the predefined function in a sequence to draw the given shape


Key Functions

1.go_to(x, y): Moves turtle to a target coordinate using velocity commands( indirect teleporting )

2.rotate(angle): Rotates the turtle by a given angle (in radians).

3.draw_square(center_x, center_y, side_length): Draws a rotated square (diamond shape).

4.draw_circle(center_x, center_y, radius): Draws a circle around the given center.

5.pen_up() / pen_down(): Controls whether the turtle draws while moving.

Future Improvements

Implement real-time pose tracking using /turtle1/pose.

Add custom shape drawing support.

Improve movement accuracy using PID controllers.
