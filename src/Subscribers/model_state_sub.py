from gazebo_msgs.msg import ModelStates, ModelState
import rospy
from geometry_msgs.msg import Pose, Twist

pose = Pose()
#print('pose:', pose)
twist = Twist()
#print('twist:', twist)
model = ModelState()
#print('model: ', model)

# Define a callback for the ModelStates message
def model_state_callback(states_msg):
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

    model_name = 'tiago' # 'tiago', 'ground_plane', 'obstacle_name'
    for i in range(0, len(states_msg.name)):
        if states_msg.name[i] == model_name:
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


    model.model_name = model_name
    model.pose = pose
    model.twist = twist
    model.reference_frame = 'world' # 'map', 'world', etc.    
    #print('model: ', model)


# Initialize the ROS Node named 'get_model_state', allow multiple nodes to be run with this name
rospy.init_node('get_model_state', anonymous=True)

# Initalize a subscriber to the "/gazebo/model_states" topic with the function "model_state_callback" as a callback
sub_state = rospy.Subscriber("/gazebo/model_states", ModelStates, model_state_callback)

# Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():
    rospy.spin()
