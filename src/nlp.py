#! /usr/bin/env python3

from __future__ import print_function
import rospy

# Brings in the SimpleActionClient
import actionlib

import pal_interaction_msgs.msg

from std_msgs.msg import String


def tts_client(text_msg):
    # Creates the SimpleActionClient, passing the type of the action to the constructotr
    client = actionlib.SimpleActionClient('tts', pal_interaction_msgs.msg.TtsAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = pal_interaction_msgs.msg.TtsGoal()
    #goal.rawtext.text = 'I am Tiago and I can talk. Wo ho. Hu ra.'
    #goal.rawtext.text = 'Ich bin Tiago and ich kann sprechen. Wo ho. Hu ra.'
    #goal.rawtext.text = 'Ich heiße Tiago and ich kann schweizer Deutsch sprechen. Wo ho. Hu ra.'
    #goal.rawtext.text = 'Das passiert, wenn ein Amerikaner versucht, Deutsch zu sprechen.'
    #goal.rawtext.text = 'Uncle Sam wants you for the US army.'
    #goal.rawtext.text = 'It seems that I cannot speak German. Why am I then in Germany?'
    #goal.rawtext.text = 'How can I get out from this lab?'
    
    goal.rawtext.text = str(text_msg)
    goal.rawtext.lang_id = 'de_DE' #'en_US' or 'de_DE'
    print(text_msg)

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult

def text_exps_callback(msg):
    result = tts_client(msg.data)

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('tts_client_py')

        #result = tts_client('I am Tiago!')

        # Initalize a subscriber to the "/camera/rgb/image_raw" topic with the function "image_callback" as a callback
        sub_text_expls = rospy.Subscriber("/text_exps", String, text_exps_callback)
        # Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
        while not rospy.is_shutdown():
            rospy.spin()
    
    except rospy.ROSInterruptException:
        print("program interrupted before completion")