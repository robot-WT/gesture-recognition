#!/home/jetson/archiconda3/envs/hand_controller/bin python3.8
import cv2
import time
import os

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist

import HandTrackingModule as htm
wCam, hCam = 640, 480

pTime = 0
detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]
rospy.init_node('webcam_display', anonymous=True)
cmd_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
cmd_msg = Twist()
while not rospy.is_shutdown():
    # print(2)
    msg =rospy.wait_for_message("fisheye", Image, timeout=0.1)
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(msg, "bgr8")
    #  print(3)
    img = detector.findHands(img)
    # print(4)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
    if len(lmList) != 0:
        fingers = []
        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)
        if (5-totalFingers) == 0:
            cmd_msg.linear.x = 1
            cmd_msg.angular.z = 0
            cmd_pub.publish(cmd_msg)
            rospy.loginfo("message have published x = %0.2f angular z = %0.2f",cmd_msg.linear.x,cmd_msg.angular.z)
        elif (5-totalFingers) == 1:
            cmd_msg.linear.x = -1
            cmd_msg.angular.z = 0
            cmd_pub.publish(cmd_msg)
            rospy.loginfo("message have published x = %0.2f angular z = %0.2f",cmd_msg.linear.x,cmd_msg.angular.z)
        elif (5-totalFingers) == 2:
            cmd_msg.linear.x = 0
            cmd_msg.angular.z = 0.5
            cmd_pub.publish(cmd_msg)
            rospy.loginfo("message have published x = %0.2f angular z = %0.2f",cmd_msg.linear.x,cmd_msg.angular.z)
        elif (5-totalFingers) == 3:
            cmd_msg.linear.x = 0
            cmd_msg.angular.z = -0.5
            cmd_pub.publish(cmd_msg)
            rospy.loginfo("message have published x = %0.2f angular z = %0.2f",cmd_msg.linear.x,cmd_msg.angular.z)
        else:
            cmd_msg.linear.x = 0
            cmd_msg.angular.z = 0
            cmd_pub.publish(cmd_msg)
            rospy.loginfo("message have published x = %0.2f angular z = %0.2f",cmd_msg.linear.x,cmd_msg.angular.z)

        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(5-totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
