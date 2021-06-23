#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

pos = dict()
def poseCallback(m):
    if m.linear_velocity == 0 and m.angular_velocity == 0:
        x = m.x
        y = m.y
        theta = m.theta
        pos[0] = x
        pos[1] = y
        pos[2] = theta


    

if __name__ == '__main__':
    goal = [0,0]
    rospy.init_node('turtlesim_pose',anonymous=True)
    sub = rospy.Subscriber('/turtle1/pose',Pose,callback = poseCallback)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=5)

    rospy.loginfo('Goal is x = {0[0]}, y = {0[1]}'.format(goal))
    run = True

    rate = rospy.Rate(1)

    counter = 0
    while not rospy.is_shutdown() and run:
        pose = Pose()
        poseCallback(pose)

        if run:
            d_x = float(pos[0] - goal[0])
            d_y = float(pos[1] - goal[1])

            rospy.loginfo('d_x + {} d_y = {} pose.x = {} pose.y = {} theta = {}'.format(d_x,d_y,pose.x,pose.y,pose.theta))

            if d_y == 0:
                d_y == 0.0001

            try:
                t1 = math.atan(d_x/d_y)
            except:
                t1 = math.pi
                if d_x < 0:
                    t1 += math.pi

            t2 = pos[2]
            rel_t = t2-t1

            twist = Twist()
            twist.angular.x = 2*rel_t
            
            pub.publish(pose)
            

            while not (int(pos[0]) == goal[0] and int(pos[1]) == goal[1]):
                twist.linear.x = 1
            
            twist.linear.x = 0


            if int(pos[0]) == goal[0] and int(pos[1]) == goal[1]:
                run = False
            counter += 1
            rospy.loginfo('Iteration No. ' + str(counter))


    rospy.spin()
    rospy.loginfo('node terminated')
    