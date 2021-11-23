from gazebo_msgs.msg import ModelStates, ModelState
import rospy
from geometry_msgs.msg import Pose, Twist
from nav_msgs.msg import Odometry

pose = Pose()
#print('pose:', pose)
twist = Twist()
#print('twist:', twist)

class Tiago:
    def __init__(self):
        self._model = ModelState()
        self._model.model_name = 'tiago'
        self._model.reference_frame = 'world' # 'map', 'world', etc.

tiago = Tiago()

class Citizen:
    def __init__(self):
        self._model = ModelState()
        self._model.model_name = 'citizen_extras_male_03'
        self._model.reference_frame = 'world' # 'map', 'world', etc.

citizen = Citizen()        

class Image:
    def __init__(self):
        self._model = ModelState()
        self._model.model_name = 'calibration_plane'
        self._model.reference_frame = 'world' # 'map', 'world', etc.                        

image = Image()

model_names = ['tiago','citizen_extras_male_03','calibration_plane']

# Define a callback for the ModelStates message
def model_state_callback(states_msg):
    for model_name in model_names:
        for i in range(0, len(states_msg.name)):
            if states_msg.name[i] == model_name:
                break

        pose = states_msg.pose[i]
        #print('pose: ', pose)
        
        twist = states_msg.twist[i]
        #print('twist: ', twist)

        if model_name == model_names[0]:
            tiago._model.pose = pose
            tiago._model.twist = twist    
            #print('tiago._model: ', tiago._model)
            #print('\n')
        elif model_name == model_names[1]:
            citizen._model.pose = pose
            citizen._model.twist = twist    
            #print('citizen._model: ', citizen._model)
            #print('\n')
        elif model_name == model_names[2]:
            image._model.pose = pose
            image._model.twist = twist    
            #print('image._model: ', tiago._model)
            #print('\n')

odom = Odometry()

# Define a callback for the ModelStates message
def odom_callback(odom_msg):
    odom.header = odom_msg.header
    odom.child_frame_id = odom_msg.child_frame_id
    odom.pose = odom_msg.pose
    odom.twist = odom_msg.twist

def get_states():
    try:
        rospy.init_node('rl_sub', anonymous=True)
    except rospy.exceptions.ROSException:
        pass
    sub_state = rospy.Subscriber("/gazebo/model_states", ModelStates, model_state_callback)

def get_odom():    
    try:
        rospy.init_node('rl_sub', anonymous=True)
    except rospy.exceptions.ROSException:
        pass
    sub_state = rospy.Subscriber("/mobile_base_controller/odom", Odometry, odom_callback)
