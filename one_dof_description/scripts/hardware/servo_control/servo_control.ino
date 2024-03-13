#include <ros.h>
#include <std_msgs/Float64.h>
#include <Servo.h>

Servo servo;
#define servo_pin 9

void servoPositionCallback(const std_msgs::Float64& msg) {
    // Convert the received command to the appropriate servo position command
    int angle = int(msg.data); // Assuming the data is in degrees
    servo.write(angle); // Write the command to your servo motor
}

ros::NodeHandle nh;
ros::Subscriber<std_msgs::Float64> sub("/joint_position_controller/command", &servoPositionCallback);

void setup() {
    nh.initNode();
    nh.subscribe(sub);

    servo.attach(servo_pin); // Assuming your servo is connected to pin 9
}

void loop() {
    nh.spinOnce();
    delay(10);
}
