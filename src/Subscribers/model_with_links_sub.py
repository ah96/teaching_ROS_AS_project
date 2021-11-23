# TO-DO  add obstacle and map class

from gazebo_msgs.msg import ModelStates, ModelState, LinkStates, LinkState
import rospy
from geometry_msgs.msg import Pose, Twist

pose = Pose()
#print('pose:', pose)
twist = Twist()
#print('twist:', twist)
link = LinkState()
#print('link: ', link)

# 'steel', 'titanium'
tiago_model = 'steel'


class Block:
    def __init__(self, model_name, link_name):
        self.model_name = model_name
        self.link_name = link_name

class Tiago:
    def __init__(self):
        self._blockListDictLen = 59
        self._links = [LinkState()] * self._blockListDictLen
        self._model = ModelState()
        self._model.model_name = 'tiago'
        self._model.reference_frame = 'world' # 'map', 'world', etc.

    _blockListDictTiagoTitanium = {
        'block_1': Block('tiago', 'base_footprint'),
        'block_2': Block('tiago', 'caster_back_left_1_link'),
        'block_3': Block('tiago', 'caster_back_left_2_link'),
        'block_4': Block('tiago', 'caster_back_right_1_link'),
        'block_5': Block('tiago', 'caster_back_right_2_link'),
        'block_6': Block('tiago', 'caster_front_left_1_link'),
        'block_7': Block('tiago', 'caster_front_left_2_link'),
        'block_8': Block('tiago', 'caster_front_right_1_link'),
        'block_9': Block('tiago', 'caster_front_right_2_link'),
        'block_10': Block('tiago', 'suspension_left_link'),
        'block_11': Block('tiago', 'wheel_left_link'),
        'block_12': Block('tiago', 'tiago::suspension_right_link'),
        'block_13': Block('tiago', 'wheel_right_link'),
        'block_14': Block('tiago', 'torso_lift_link'),
        'block_15': Block('tiago', 'arm_1_link'),
        'block_16': Block('tiago', 'arm_2_link'),
        'block_17': Block('tiago', 'arm_3_link'),
        'block_18': Block('tiago', 'arm_4_link'),
        'block_19': Block('tiago', 'arm_5_link'),
        'block_20': Block('tiago', 'arm_6_link'),
        'block_21': Block('tiago', 'arm_7_link'),
        'block_22': Block('tiago', 'hand_index_abd_link'),
        'block_23': Block('tiago', 'hand_index_virtual_1_link'),
        'block_24': Block('tiago', 'hand_index_flex_1_link'),
        'block_25': Block('tiago', 'hand_index_virtual_2_link'),
        'block_26': Block('tiago', 'hand_index_flex_2_link'),
        'block_27': Block('tiago', 'hand_index_virtual_3_link'),
        'block_28': Block('tiago', 'hand_index_flex_3_link'),
        'block_29': Block('tiago', 'hand_index_link'),
        'block_30': Block('tiago', 'hand_little_abd_link'),
        'block_31': Block('tiago', 'hand_little_virtual_1_link'),
        'block_32': Block('tiago', 'hand_little_flex_1_link'),
        'block_33': Block('tiago', 'hand_little_virtual_2_link'),
        'block_34': Block('tiago', 'hand_little_flex_2_link'),
        'block_35': Block('tiago', 'hand_little_virtual_3_link'),
        'block_36': Block('tiago', 'hand_little_flex_3_link'),
        'block_37': Block('tiago', 'hand_middle_abd_link'),
        'block_38': Block('tiago', 'hand_middle_virtual_1_link'),
        'block_39': Block('tiago', 'hand_middle_flex_1_link'),
        'block_40': Block('tiago', 'hand_middle_virtual_2_link'),
        'block_41': Block('tiago', 'hand_middle_flex_2_link'),
        'block_42': Block('tiago', 'hand_middle_virtual_3_link'),
        'block_43': Block('tiago', 'hand_middle_flex_3_link'),
        'block_44': Block('tiago', 'hand_mrl_link'),
        'block_45': Block('tiago', 'hand_ring_abd_link'),
        'block_46': Block('tiago', 'hand_ring_virtual_1_link'),
        'block_47': Block('tiago', 'hand_ring_flex_1_link'),
        'block_48': Block('tiago', 'hand_ring_virtual_2_link'),
        'block_49': Block('tiago', 'hand_ring_flex_2_link'),
        'block_50': Block('tiago', 'hand_ring_virtual_3_link'),
        'block_51': Block('tiago', 'hand_ring_flex_3_link'),
        'block_52': Block('tiago', 'hand_thumb_abd_link'),
        'block_53': Block('tiago', 'hand_thumb_virtual_1_link'),
        'block_54': Block('tiago', 'hand_thumb_flex_1_link'),
        'block_55': Block('tiago', 'hand_thumb_virtual_2_lin'),
        'block_56': Block('tiago', 'hand_thumb_flex_2_link'),
        'block_57': Block('tiago', 'hand_thumb_link'),
        'block_58': Block('tiago', 'head_1_link'),
        'block_59': Block('tiago', 'head_2_link')
    }

    _blockListDictTiagoSteel = {
    'block_1': Block('tiago', 'base_footprint'),
    'block_2': Block('tiago', 'caster_back_left_1_link'),
    'block_3': Block('tiago', 'caster_back_left_2_link'),
    'block_4': Block('tiago', 'caster_back_right_1_link'),
    'block_5': Block('tiago', 'caster_back_right_2_link'),
    'block_6': Block('tiago', 'caster_front_left_1_link'),
    'block_7': Block('tiago', 'caster_front_left_2_link'),
    'block_8': Block('tiago', 'caster_front_right_1_link'),
    'block_9': Block('tiago', 'caster_front_right_2_link'),
    'block_10': Block('tiago', 'suspension_left_link'),
    'block_11': Block('tiago', 'wheel_left_link'),
    'block_12': Block('tiago', 'tiago::suspension_right_link'),
    'block_13': Block('tiago', 'wheel_right_link'),
    'block_14': Block('tiago', 'torso_lift_link'),
    'block_15': Block('tiago', 'arm_1_link'),
    'block_16': Block('tiago', 'arm_2_link'),
    'block_17': Block('tiago', 'arm_3_link'),
    'block_18': Block('tiago', 'arm_4_link'),
    'block_19': Block('tiago', 'arm_5_link'),
    'block_20': Block('tiago', 'arm_6_link'),
    'block_21': Block('tiago', 'arm_7_link'),
    'block_22': Block('tiago', 'tiago::gripper_left_finger_link'),
    'block_23': Block('tiago', 'tiago::gripper_right_finger_link'),
    'block_24': Block('tiago', 'head_1_link'),
    'block_25': Block('tiago', 'head_2_link')
    }


tiago = Tiago()    

# Define a callback for the LinkStates message
def link_state_callback(states_msg):
    index = 0

    if tiago_model == 'titanium':
        for block in tiago._blockListDictTiagoTitanium.itervalues():
            link_name = str(block.link_name)
            for i in range(0, len(states_msg.name)):
                if states_msg.name[i] == link_name:
                    break

            pose = states_msg.pose[i]
            #print('pose: ', pose)

            twist = states_msg.twist[i]
            #print('twist: ', twist)

            link.link_name = link_name
            link.pose = pose
            link.twist = twist
            link.reference_frame = 'world' # 'map', 'world', etc.    
            #print('link: ', link)

            tiago._links[index] = link
            index+=1

    elif tiago_model == 'steel':
        for block in tiago._blockListDictTiagoSteel.itervalues():
            link_name = str(block.link_name)
            for i in range(0, len(states_msg.name)):
                if states_msg.name[i] == link_name:
                    break

            pose = states_msg.pose[i]
            #print('pose: ', pose)

            twist = states_msg.twist[i]
            #print('twist: ', twist)

            link.link_name = link_name
            link.pose = pose
            link.twist = twist
            link.reference_frame = 'world' # 'map', 'world', etc.    
            #print('link: ', link)

            tiago._links[index] = link
            index+=1

    print('tiago._links: ', tiago._links)
    print('\n')    


# Define a callback for the ModelStates message
def model_state_callback(states_msg):
    model_name = 'tiago'
    for i in range(0, len(states_msg.name)):
        if states_msg.name[i] == model_name:
            break

    pose = states_msg.pose[i]
    #print('pose: ', pose)
    
    twist = states_msg.twist[i]
    #print('twist: ', twist)

    tiago._model.pose = pose
    tiago._model.twist = twist    
    print('tiago._model: ', tiago._model)
    print('\n')


# Initialize the ROS Node named 'model_with_links_state', allow multiple nodes to be run with this name
rospy.init_node('model_with_links_state', anonymous=True)

# Initalize a subscriber to the "/gazebo/link_states" topic with the function "link_state_callback" as a callback
sub_link_state = rospy.Subscriber("/gazebo/link_states", LinkStates, link_state_callback)

# Initalize a subscriber to the "/gazebo/model_states" topic with the function "model_state_callback" as a callback
sub_model_state = rospy.Subscriber("/gazebo/model_states", ModelStates, model_state_callback)

# Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():
    rospy.spin()
