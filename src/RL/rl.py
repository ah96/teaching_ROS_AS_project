from rl_sub import tiago, citizen, image, get_states, odom, get_odom
import time
from gazebo_msgs.msg import ModelState 
from geometry_msgs.msg import Twist

from rl_pub import publish_state, publish_vel

# receive info about Gazebo model states
'''
def getStates():
    get_states()
    time.sleep(0.05)
    print('tiago._model: ', tiago._model)
    print('citizen._model: ', citizen._model)
    print('image._model: ', image._model)
    
getStates()    
'''

# receive odometry data
'''
def getOdom():
    get_odom()
    time.sleep(0.1)
    print('odometry data: ', odom)

getOdom()
'''

# send state data/commands to Gazebo model
'''
def sendState(model_state):
    publish_state(model_state)
    time.sleep(0.3)
    publish_state(model_state)

model_state = ModelState()
model_state.model_name = 'tiago'
model_state.reference_frame = 'world'
model_state.pose.position.x = 0.0
model_state.pose.position.y = 0.0
model_state.pose.position.z = 0
model_state.pose.orientation.x = 0
model_state.pose.orientation.y = 0
model_state.pose.orientation.z = 0
model_state.pose.orientation.w = 0
model_state.twist.linear.x = 0
model_state.twist.linear.y = 0
model_state.twist.linear.z = 0
model_state.twist.angular.x = 0
model_state.twist.angular.y = 0
model_state.twist.angular.z = 0    
sendState(model_state)
'''

# send command velocities
'''
def sendVel(twist):
    publish_vel(twist)
    time.sleep(0.3)
    publish_vel(twist)

twist = Twist()
twist.linear.x = 0.5
twist.linear.y = 0
twist.linear.z = 0
twist.angular.x = 0
twist.angular.y = 0
twist.angular.z = 0    
sendVel(twist)
'''


# your RL code...