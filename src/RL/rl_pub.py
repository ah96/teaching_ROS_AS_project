import rospy
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Twist
    
def publish_state(model_state):
    try:
        rospy.init_node('rl_pub', anonymous=True)
    except rospy.exceptions.ROSException:
        pass
    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
    pub.publish(model_state)

def publish_vel(twist):
    try:
        rospy.init_node('rl_pub', anonymous=True)
    except rospy.exceptions.ROSException:
        pass
    pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=10)
    pub.publish(twist)
    