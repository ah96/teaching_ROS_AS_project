from gazebo_msgs.msg import LinkStates, LinkState
import rospy
from geometry_msgs.msg import Pose, Twist

pose = Pose()
#print('pose:', pose)
twist = Twist()
#print('twist:', twist)
link = LinkState()
#print('link: ', link)

# Define a callback for the LinkStates message
def link_state_callback(states_msg):
    '''
    print('type(states_msg): ', type(states_msg))
    print('states_msg.name: ', states_msg.name)
    print('states_msg.pose: ', states_msg.pose)
    print('states_msg.twist: ', states_msg.twist)
    print('\n')
    '''

    '''
    print('type(states_msg.name): ', type(states_msg.name))
    print('type(states_msg.pose): ', type(states_msg.pose))
    print('type(states_msg.twist): ', type(states_msg.twist))
    print('\n')
    '''

    link_name = 'tiago::base_footprint' # 'ground_plane::link', 'tiago::base_footprint', tiago::caster_back_left_1_link', 'tiago::caster_back_left_2_link', ...
    for i in range(0, len(states_msg.name)):
        if states_msg.name[i] == link_name:
            break

    pose = states_msg.pose[i]
    #print('pose: ', pose)
    #print('type(pose): ', type(pose))
    #print('pose.position: ', pose.position)
    #print('pose.orientation: ', pose.orientation)
    
    twist = states_msg.twist[i]
    #print('twist: ', twist)
    #print('type(twist): ', type(twist))
    #print('twist.linear: ', twist.linear)
    #print('twist.angular: ', twist.angular)
    #print('\n')


    link.link_name = link_name
    link.pose = pose
    link.twist = twist
    link.reference_frame = 'world' # 'map', 'world', etc.    
    #print('link: ', link)
    #print('\n')


# Initialize the ROS Node named 'get_link_state', allow multiple nodes to be run with this name
rospy.init_node('get_link_state', anonymous=True)

# Initalize a subscriber to the "/gazebo/link_states" topic with the function "link_state_callback" as a callback
sub_state = rospy.Subscriber("/gazebo/link_states", LinkStates, link_state_callback)

# Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():
    rospy.spin()
