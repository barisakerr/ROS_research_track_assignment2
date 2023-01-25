## ROS_research_track_assignment2 ##

# Description #

The purpose of the Project to control the robot movement on x and y axis. When the program launched user will see four main windows. First two windows are Gazebo and sim2.rviz, third and the fourth windows are printer.py and action_usr.py windows. The movement of the robot will observe in the Gazebo window. In the Gazebo window there are some outside walls for determine the possible movement area of the robot and there are also inside walls these walls can consider as an obstacle. Depends on to the given coordinates by the user, if the robot will go to the one of those walls, it tries to exceed the wall by turning and moving and after to focus to the target position and then again to move through to the target location.


# Installing #

For run the program the xterm libray should be downloaded. By writing the folowing command on to the terminal window the xterm package can be install. Purpose of that libray is to prints outputs of the nodes on a new terminal window.

	sudo apt-get install xterm -y

Navigate to your ROS workspace 'src' folder and clone this repository using the following command:
	
	git clone <link of the repository>

Then, navigate to the workspace directory and run the following command to build the package:

	catkin_make

# Running #

You can run the program with:
```bash
roslaunch assignment_2_2022 assignment_2.launch
```
# How it's works #

Inside of the scripts folder there are six .py files. Three of them main files of the program which are, go_to_point_service.py, wall_follow_serice.py and the other one bug_as.py. 

Purpose of the go_to_point_service.py is to provides the expected movement for the robot by using the laser sensor and odometry. By using the data which are coming from the robot’s sensors the current position and the orientation of the robot could be determine. the other one is to move the robot to the target position as a straight and the other one when the robot will reach to the target position the robot will stops. 

-	When the state is 0 robot rotates itself with fix_yaw() function to the direction of target position. 
-	When the state is 1 robot moves through to the target position of the robot with the go_straight_ahead() function. 
-	When the state is 2 robot stops by using done() function, the linear and the angular velocities become zero.  


Purpose of the wall_follow_service.py is to manage the movements of the robot and to provides to reach to the target position correctly in case of the robot will encounter with the wall. There are three main directions for the robot in this program file, front, right and left. Inside of the code when the robot become so close to the wall the sensors perceive this situation and depends on this situation robot rotating to the left and it tries to follow the wall. There are three main states one of them finding the wall, turning to the left and the other one is to follow the wall.

-	When the state is 0 robot tries to find the wall with the given linear and the angular velocity values.
-	When the state is 1 robot turns left. 
-	When the state is 2 robot follows the wall. 

bug_as.py is combine the go_to_point_service.py and wall_follow_service.py there are three main states for this node, first one is 0 which is for to move the robot directly to the target position. 

-	When the state become 0 then the go_to_point_service.py become true and wall_follow_service.py become false so just the go_to_point_service.py works and the robot can move through to the target location. 

-	When the state become 1 then the go_to_point_service.py becomes false and wall_follow_service.py becomes true so just the wall_follow_service.py works and the robot rotates itself and follows the wall and try to end the wall. 

-	When the state become 2 then the go_to_point_service.py and wall_follow_service.py becomes both false, both program files not working in this state because the robot has been already reached to the target position. 

The other three py. files which are located inside of the scripts folder are, action.usr.py, printer.py and service.goal.py. 

To provide the expected steps in the A part of the assignment the action.usr.py file has been created. One of the purposes of that node is to publish the position and the velocity values of the robot by creating a custom message. For that purpose the custom message has been create as posxy_velxy = Posxy_velxy() after this creation, position x, y and the velocity x, y had been assigned to the custom message. After then the custom message had been published by using the pub.publish() function. The client had been created by using the action_client() function to allows the user enters the position inputs of the robot for the direction x and direction y and also it allows to user can enter a “c” input to cancel the movement of the robot.  In case the user will enters “c” as a x position and enters “c” as a y position then the movement process will stop. Otherwise, the inputs which are entered by the user will converting from string to the float and these float values assigning as a sending value and these sending values assigning as a goal position values of the robot for x and y direction. These assigning are made to the goal() function and the goal has been send to the action_client(). 

To provide the expected steps in the B part of the assignment the service.goal.py node has been created. The purpose of that node is to print the number of reached goals and number of cancelled goals. There are two main statuses, one of them is 2 and the other one is 3. 

-	When the status become 2, means that goal has been cancelled and the program counts +1 to increase the cancelled goal value. 

-	When the status become 3, means that goal has been reached and the program counts +1 to increase the reached goal value. 

To provide the expected steps in the C part of the assignment the printer.py node has been created. The purpose of this program file is to subscribe the robot’s position and it’s velocity by using the custom message and prints the distance between the robot and the target position and the average speed of the robot. The code is taking the target position values which has been entered by the user to the action.usr.py by using the rospy.get_param() function for x and y positions both. Then the actual x and y position values of the robot taking from the message. Depends on this position info, the direct distance between the robot and the target position has been computing.  Also, the robot’s actual x and y velocities getting from the message. Then the actual velocity values which are coming from the message has been computing to find the average velocity of the robot. At the end the distance between the robot and the target position and the average speed of the robot is printing on the printer screen. The frequency of the screen has been settled as a 1 per second that is why user supposed to see the distance between the robot and the target value and the average speed of the robot value in every 1 second on the printer screen. 

# Flow Chart #

<img width="635" alt="Screen Shot 2023-01-25 at 22 54 18" src="https://user-images.githubusercontent.com/83571132/214700418-0dc0bb39-3a97-4036-9688-9e03311a72ac.png">


