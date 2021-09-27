import rospy
from gazebo_msgs.msg import LinkState, ModelState
import random

# 'steel', 'titanium'
tiago_model = 'steel'

class Block:
    def __init__(self, name, relative_entity_name):
        self.model_name = name
        self.link_name = relative_entity_name

blockListDictTiagoTitanium = {
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

blockListDictTiagoSteel = {
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


def link_state_publisher():
    model_pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
    
    link_pub = rospy.Publisher('/gazebo/set_link_state', LinkState, queue_size=10)

    rospy.init_node('set_model_with_links_state', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    if tiago_model == 'titanium':
        blockListDict = blockListDictTiagoTitanium
    elif tiago_model == 'steel':
        blockListDict = blockListDictTiagoSteel    
    
    while not rospy.is_shutdown():
        model_state = ModelState()
        model_state.model_name = 'tiago' # 'tiago', 'ground_plane', 'obstacle_name'
        model_state.reference_frame = 'world'
        model_state.pose.position.x = 0
        model_state.pose.position.y = 0
        model_state.pose.position.z = 0
        model_state.pose.orientation.x = 0
        model_state.pose.orientation.y = 0
        model_state.pose.orientation.z = 0.0
        model_state.pose.orientation.w = 0
        model_state.twist.linear.x = 0
        model_state.twist.linear.y = 0
        model_state.twist.linear.z = 0
        model_state.twist.angular.x = 0
        model_state.twist.angular.y = 0
        model_state.twist.angular.z = 0

        link_state = LinkState()
        index = random.randint(0, len(blockListDict) - 1)
        link_state.link_name = list(blockListDict.values())[index].link_name
        link_state.reference_frame = 'world'
        link_state.pose.position.x = 0
        link_state.pose.position.y = 0
        link_state.pose.position.z = 0
        link_state.pose.orientation.x = 0
        link_state.pose.orientation.y = 0
        link_state.pose.orientation.z = 0.0
        link_state.pose.orientation.w = 0
        link_state.twist.linear.x = 15.0
        link_state.twist.linear.y = 0
        link_state.twist.linear.z = 0
        link_state.twist.angular.x = 0
        link_state.twist.angular.y = 0
        link_state.twist.angular.z = 0

        print('link_state.link_name: ', link_state.link_name)

        #rospy.loginfo(model_state)
        model_pub.publish(model_state)
        link_pub.publish(link_state)
        rate.sleep()

if __name__ == '__main__':
    try:
        link_state_publisher()
    except rospy.ROSInterruptException:
        pass