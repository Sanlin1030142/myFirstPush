#!/usr/bin/env python

# set the execute environment

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String		# for topic

def talker():
    # set the conclu. between node and topic
    # syntex
# publisher=rospy.Publisher(topic_name, msg_class, queue_size)
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # initial the node
    # anonymous==> add randon number after node_name

    
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.


    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

# execute the "talker" 

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
