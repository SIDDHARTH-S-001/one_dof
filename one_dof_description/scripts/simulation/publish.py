#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def publish_joint_position(joint_value):
    # Initialize ROS node
    rospy.init_node('joint_position_publisher', anonymous=True)

    # Create a publisher for the joint position command
    joint_position_pub = rospy.Publisher('/joint_position_controller/command', Float64, queue_size=10)

    # Wait for some time to allow publishers to register
    rospy.sleep(1.0)

    # Create a Float64 message with the specified joint value
    joint_position_msg = Float64(data=joint_value)

    # Publish the joint position message
    joint_position_pub.publish(joint_position_msg)

if __name__ == '__main__':
    try:
        # Replace 1.0 with the desired joint position value
        joint_value = 0.0
        publish_joint_position(joint_value)
    except rospy.ROSInterruptException:
        pass
