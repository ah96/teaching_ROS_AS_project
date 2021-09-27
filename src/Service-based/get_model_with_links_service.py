from gazebo_msgs.srv import GetModelState
import rospy

# 'steel', 'titanium'
tiago_model = 'steel'

class Block:
    def __init__(self, name, relative_entity_name):
        self._name = name
        self._relative_entity_name = relative_entity_name

class Tiago:

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

    def show_gazebo_models(self):
        try:
            model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
            if tiago_model == 'titanium':
                for block in self._blockListDictTiagoTitanium.itervalues():
                    blockName = str(block._name)
                    resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
                    print('\n')
                    print('Status.success = ', resp_coordinates.success)
                    print(blockName)
                    print("Model: " + str(block._name))
                    print("Link: " + str(block._relative_entity_name)) 
                    print("position.x: " + str(resp_coordinates.pose.position.x))
                    print("position.y: " + str(resp_coordinates.pose.position.y))
                    print("position.z: " + str(resp_coordinates.pose.position.z))
                    print("orientation.x: " + str(resp_coordinates.pose.orientation.x))
                    print("orientation.y: " + str(resp_coordinates.pose.orientation.y))
                    print("orientation.z: " + str(resp_coordinates.pose.orientation.z))
                    print("orientation.w: " + str(resp_coordinates.pose.orientation.w))
                    print("linear.x: " + str(resp_coordinates.twist.linear.x))
                    print("linear.y: " + str(resp_coordinates.twist.linear.y))
                    print("linear.z: " + str(resp_coordinates.twist.linear.z))
                    print("angular.x: " + str(resp_coordinates.twist.angular.x))
                    print("angular.y: " + str(resp_coordinates.twist.angular.y))
                    print("angular.z: " + str(resp_coordinates.twist.angular.z))

            elif tiago_model == 'steel':
                for block in self._blockListDictTiagoSteel.itervalues():
                    blockName = str(block._name)
                    resp_coordinates = model_coordinates(blockName, block._relative_entity_name)
                    print('\n')
                    print('Status.success = ', resp_coordinates.success)
                    print(blockName)
                    print("Model: " + str(block._name))
                    print("Link: " + str(block._relative_entity_name)) 
                    print("position.x: " + str(resp_coordinates.pose.position.x))
                    print("position.y: " + str(resp_coordinates.pose.position.y))
                    print("position.z: " + str(resp_coordinates.pose.position.z))
                    print("orientation.x: " + str(resp_coordinates.pose.orientation.x))
                    print("orientation.y: " + str(resp_coordinates.pose.orientation.y))
                    print("orientation.z: " + str(resp_coordinates.pose.orientation.z))
                    print("orientation.w: " + str(resp_coordinates.pose.orientation.w))
                    print("linear.x: " + str(resp_coordinates.twist.linear.x))
                    print("linear.y: " + str(resp_coordinates.twist.linear.y))
                    print("linear.z: " + str(resp_coordinates.twist.linear.z))
                    print("angular.x: " + str(resp_coordinates.twist.angular.x))
                    print("angular.y: " + str(resp_coordinates.twist.angular.y))
                    print("angular.z: " + str(resp_coordinates.twist.angular.z))        

        except rospy.ServiceException as e:
            rospy.loginfo("Get Model State service call failed:  {0}".format(e))


#if __name__ == '__main__':
#rospy.init_node("get_tiago_state", anonymous=True)
tiago = Tiago()
tiago.show_gazebo_models()