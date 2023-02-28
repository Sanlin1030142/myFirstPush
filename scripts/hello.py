#!/usr/bin/env python

import rospy				# import rospy module

rospy.init_node('hello_python_node')	# initial hello_python_node

# rospy.loginfo('Hello World')		# print Hello World

while not rospy.is_shutdown() :		# exe below before rospy end
  rospy.loginfo('Hello World')		# print Hello World
  rospy.sleep(1)			# every one second
