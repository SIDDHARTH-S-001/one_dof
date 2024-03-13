#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from tkinter import Tk, Scale, Label, DoubleVar, Button
from functools import partial

def publish_joint_position(joint_value, joint_position_pub):
    # Create a Float64 message with the specified joint value
    joint_position_msg = Float64(data=joint_value)

    # Publish the joint position message
    joint_position_pub.publish(joint_position_msg)

def slider_callback(value, scale_var, joint_position_pub):
    scale_var.set(value)
    scale_var = scale_var*1/180
    publish_joint_position(value, joint_position_pub)

def main():
    # Initialize ROS node
    rospy.init_node('joint_position_publisher', anonymous=True)

    # Create a publisher for the joint position command
    joint_position_pub = rospy.Publisher('/joint_position_controller/command', Float64, queue_size=10)

    # Wait for some time to allow publishers to register
    rospy.sleep(1.0)

    # Create the Tkinter GUI window
    root = Tk()
    root.title("Joint Position Publisher")

    # Create a DoubleVar to store the joint value
    scale_var = DoubleVar()

    # Create a slider
    scale = Scale(root, from_=-180.0, to=180.0, orient="horizontal", variable=scale_var, label="Joint Value", length=300)
    scale.pack(padx=10, pady=10)

    # Create a label to display the current joint value
    label = Label(root, text=f"Joint Value: {scale_var.get()}")
    label.pack(pady=10)

    # Create a callback function for the slider
    slider_callback_func = partial(slider_callback, scale_var=scale_var, joint_position_pub=joint_position_pub)
    scale.config(command=slider_callback_func)

    # Create a button to publish the current slider value
    publish_button = Button(root, text="Publish", command=lambda: publish_joint_position(scale_var.get(), joint_position_pub))
    publish_button.pack(pady=10)

    # Update the label text based on the slider value
    def update_label():
        label.config(text=f"Joint Value: {scale_var.get()}")
        root.after(100, update_label)

    update_label()

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
