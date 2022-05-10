#! /usr/bin/env python3

from __future__ import print_function
import rospy

# Brings in the SimpleActionClient
import actionlib

import sys

import pal_interaction_msgs.msg

def tts_client():
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
    goal.rawtext.text = 'Uncle Sam wants you for the US army.'
    #goal.rawtext.text = 'It seems that I cannot speak German. Why am I then in Germany?'
    #goal.rawtext.text = 'How can I get out from this lab?'
    goal.rawtext.lang_id = 'en_US'

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('tts_client_py')
        result = tts_client()
        #print("Result:", ', '.join([str(n) for n in result.sequence]))
    except rospy.ROSInterruptException:
        print("program interrupted before completion")