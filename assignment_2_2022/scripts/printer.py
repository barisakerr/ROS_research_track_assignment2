#! /usr/bin/env python

import rospy
import math
import time
from assignment_2_2022.msg import Posxy_velxy
from colorama import init
init()
from colorama import Fore, Back, Style

class PrintInfo:
    def __init__(self):
        # Get the publish frequency parameter
        self.frequency = rospy.get_param("frequency")

        # Last time the info was printed
        self.print_last = 0

        # Subscriber to the position and velocity topic
        self.sub_pos = rospy.Subscriber("/posxy_velxy", Posxy_velxy, self.posvel_callback)

    def posvel_callback(self, msg):
        
        period = (1.0/self.frequency) * 1000 # Compute time period in milliseconds
         
        current_time = time.time() * 1000 # Get current time in milliseconds

        # Check if the current time minus the last printed time is greater than the period
        if current_time - self.print_last > period:
            
            target_x_position = rospy.get_param("des_pos_x") # getting the desired positions on x axis from ROS parameters 
            target_y_position = rospy.get_param("des_pos_y") # getting the desired positions on y axis from ROS parameters 

            robot_x = msg.msg_pos_x # actual position of the robot on x axis is getting from message 
            robot_y = msg.msg_pos_y # actual position of the robot on y axis is getting from message 

            distance_to_target = round(math.dist([target_x_position, target_y_position], [robot_x, robot_y]),2) # Computing the distance between the desired and actual positions (hypotenus)
            
            vel_x = msg.msg_vel_x # actual velocity of the robot on x axis is getting from message 
            vel_y = msg.msg_vel_y # actual velocity of the robot on y axis is getting from message           

            average_speed = round(math.sqrt(vel_x**2 + vel_y**2),2) # Computing the average of the actual speeds

            # Print the distance and speed information
            rospy.loginfo(Fore.BLACK + "Distance to the target: %s [m]", distance_to_target) # printing the distance between the robot and the target 
            rospy.loginfo(Fore.BLUE + "Robot's average speed: %s [m/s]", average_speed) # printing the robot's average speed  

            # Update the last printed time
            self.print_last = current_time

def main():
	
    # Suppress the timestamps from the log messages
    #rospy.set_param('/rosconsole/formatter/time', 'none') I tried to delete time values from scren but it didn`t work	
    
    # Initialize the node
    rospy.init_node('printer')
    
    # Create an instance of the PrintInfo class
    printer = PrintInfo()
    
    # Wait for messages
    rospy.spin()

if __name__ == "__main__":
    main()

