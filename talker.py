#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

pub = rospy.Publisher('chatter',String,queue_size = 10)


#creates a new node named talker
rospy.init_node('talker', anonymous = True)

rate = rospy.Rate(1)

i = 0


    s = 'hello world {}'.format(i)
    rospy.loginfo(s)
    pub.publish(s)
    rate.sleep()
    i = i + 1