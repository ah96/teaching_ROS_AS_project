import rospy
from gazebo_msgs.msg import ModelState 

def model_state_publisher():
    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
    
    rospy.init_node('set_model_state', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        model_state = ModelState()
        model_state.model_name = 'tiago'
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
        model_state.twist.angular.z = 5.0

        
        #rospy.loginfo(model_state)
        pub.publish(model_state)
        rate.sleep()

if __name__ == '__main__':
    try:
        model_state_publisher()
    except rospy.ROSInterruptException:
        pass