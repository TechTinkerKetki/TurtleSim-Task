import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
import time
import math

class TurtleDraw(Node):
    def __init__(self):
        super().__init__('turtle_draw')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')
        
        self.current_x = 5.0 # Assuming starting position is (5,5)
        self.current_y = 5.0
        self.current_theta = 0.0  # Facing right
        self.pen_is_down = True

    def set_pen(self, r=255, g=255, b=255, width=2, off=False):
        """Controls pen color, width, and up/down state."""
        while not self.pen_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for pen service...')
        req = SetPen.Request()
        req.r = r
        req.g = g
        req.b = b
        req.width = width
        req.off = off
        self.pen_is_down = not off
        self.pen_client.call_async(req)

    def go_to(self, x, y, speed=1.5):
        """Moves turtle to a specific (x, y) coordinate."""
        msg = Twist()
        distance = math.sqrt((x - self.current_x) ** 2 + (y - self.current_y) ** 2)
        angle_to_target = math.atan2(y - self.current_y, x - self.current_x)

        # Rotate towards the target
        self.rotate(angle_to_target - self.current_theta)

        # Move forward
        msg.linear.x = speed
        duration = distance / speed
        start_time = time.time()
        while time.time() - start_time < duration:
            self.publisher_.publish(msg)

        msg.linear.x = 0.0
        self.publisher_.publish(msg)

        # Update current position
        self.current_x = x
        self.current_y = y
        self.current_theta = angle_to_target

    def rotate(self, angle, speed=1.0):
        """Rotates the turtle by the given angle (radians)."""
        msg = Twist()
        msg.angular.z = speed if angle > 0 else -speed
        duration = abs(angle) / speed
        start_time = time.time()

        while time.time() - start_time < duration:
            self.publisher_.publish(msg)

        msg.angular.z = 0.0
        self.publisher_.publish(msg)

        # Update current theta
        self.current_theta += angle

    def draw_square(self, center_x, center_y, side_length):
        """Draws a diamond (rotated square)."""
        half_side = side_length / math.sqrt(2)
        points = [
            (center_x, center_y + half_side),
            (center_x + half_side, center_y),
            (center_x, center_y - half_side),
            (center_x - half_side, center_y),
        ]
        self.go_to(*points[0])
        for i in range(1, len(points)):
            self.go_to(*points[i])
        self.go_to(*points[0])  # Close the shape

    def draw_circle(self, center_x, center_y, radius, speed=1.0):
        """Moves to a point and draws a circle."""
        
    # Move to the starting position (rightmost edge of the circle)
        self.go_to(center_x + radius, center_y)

    # Ensure the turtle faces upward (tangential to the circle)
        self.rotate(math.pi / 2)
        msg = Twist()
        msg.linear.x = speed
        msg.angular.z = speed / radius
        duration = (2 * math.pi * radius) / speed
        start_time = time.time()

        while time.time() - start_time < duration:
            self.publisher_.publish(msg)

        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

    def pen_up(self):
        self.set_pen(off=True)

    def pen_down(self):
        self.set_pen(off=False)

def main(args=None):
    rclpy.init(args=args)
    turtle_draw = TurtleDraw()
    print('IVDC2 node is running')
    
    # Execute drawing
    turtle_draw.pen_up()
    turtle_draw.go_to(5,7)
    turtle_draw.pen_down()
    turtle_draw.draw_square(5.0,5.0,2.82)
    turtle_draw.pen_up()
    turtle_draw.go_to(6,6)
    turtle_draw.rotate(1.57)
    turtle_draw.pen_down()
    turtle_draw.go_to(8,8)
    turtle_draw.pen_up()
    turtle_draw.go_to(9,8)
    turtle_draw.pen_down()
    turtle_draw.draw_circle(8,8,1)
    turtle_draw.pen_up()
    turtle_draw.go_to(6,4)
    turtle_draw.rotate(1.57)
    turtle_draw.pen_down()
    turtle_draw.go_to(8,2)
    turtle_draw.pen_up()
    turtle_draw.go_to(9,2)
    turtle_draw.pen_down()
    turtle_draw.draw_circle(8,2,1)
    turtle_draw.pen_up()
    turtle_draw.go_to(4,4)
    turtle_draw.rotate(1.57)
    turtle_draw.pen_down()
    turtle_draw.go_to(2,2)
    turtle_draw.pen_up()
    turtle_draw.go_to(3,2)
    turtle_draw.pen_down()
    turtle_draw.draw_circle(2,2,1)
    turtle_draw.pen_up()
    turtle_draw.go_to(4,6)
    turtle_draw.rotate(1.57)
    turtle_draw.pen_down()
    turtle_draw.go_to(2,8)
    turtle_draw.pen_up()
    turtle_draw.go_to(3,8)
    turtle_draw.pen_down()
    turtle_draw.draw_circle(2,8,1)


    turtle_draw.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
