#!/usr/bin/env python

import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion
import sys
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import subprocess
def countPoint():
    p = subprocess.run(['timeout', '2s', 'rosrun', 'find_object_2d', 'find_object_2d', 'image:=/camera/rgb/image_raw', '>', 'test.txt'])
        text_file = open("test.txt", "r")
        count = 0
        while(True):
            line = text_file.readline()
                x = line.split()
                breakTime = False
                for i in range (0, len(x)):
                    if(x[i]=="descriptors"):
                        if(x[i-1]!="Extracting"):
                            count= int(x[i-1])
                            breakTime = True
                            break
                if(breakTime == True):
                    break
        return count

test = countPoint()
print(test)

class navigate():
    def __init__(self):

        self.goal_sent = False

	# What to do if shut down (e.g. Ctrl-C or failure)
	rospy.on_shutdown(self.shutdown)
	
	# Tell the action client that we want to spin a thread by default
	self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	rospy.loginfo("Wait for the action server to come up")

	# Allow up to 5 seconds for the action server to come up
	self.move_base.wait_for_server(rospy.Duration(5))

    def goto(self, pos, quat):

        # Send a goal
        self.goal_sent = True
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),
                                     Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

	# Start moving
        self.move_base.send_goal(goal)

	# Allow TurtleBot up to 60 seconds to complete task
	success = self.move_base.wait_for_result(rospy.Duration(60)) 

        state = self.move_base.get_state()
        result = False

        if success and state == GoalStatus.SUCCEEDED:
            result = True
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        rospy.init_node('nav_test', anonymous=False)
        navigator = nagivate()

	# Change these values for different locations on the map
        position = {'x': 1.22, 'y' : 2.56}
        quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : 1.000}

        success = navigator.goto(position, quaternion)

        if success:
            rospy.loginfo("Reached destination")
        else:
            rospy.loginfo("Failed to reach destination")

        # Sleep to give the last log messages time to be sent
        rospy.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C, Quitting")

