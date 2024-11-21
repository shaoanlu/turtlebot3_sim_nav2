import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import random


class AutonomousNavigator(Node):
    def __init__(self):
        """
        This node is a random goal sender that automatically send a new position to /goal_pose
        """
        super().__init__('autonomous_navigator')
        self.goal_interval_sec = 5.0
        self.publisher = self.create_publisher(PoseStamped, '/goal_pose', 10)
        # Send a goal every X seconds where X is defined in self.goal_interval_sec
        self.timer = self.create_timer(self.goal_interval_sec, self.send_random_goal)

    def send_random_goal(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.header.stamp = self.get_clock().now().to_msg()

        # Generate random goal coordinates within a range
        goal.pose.position.x = random.uniform(-2.0, 2.0)
        goal.pose.position.y = random.uniform(-2.0, 2.0)
        goal.pose.orientation.z = 1.0  # Face forward
        goal.pose.orientation.w = 0.0

        self.get_logger().info(f"Sending goal: x={goal.pose.position.x}, y={goal.pose.position.y}")
        self.publisher.publish(goal)


def main(args=None):
    rclpy.init(args=args)
    node = AutonomousNavigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
