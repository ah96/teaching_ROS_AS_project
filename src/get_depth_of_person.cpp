#include <ros/ros.h>
#include <pal_detection_msgs/Detections2d.h>
#include <sensor_msgs/Image.h>
#include <iostream>


class ROI
{
    // Access specifier
    public:
 
    // coordinates of the top left corner of the box
    int x;
    int y;

    // width of the box
    int width;

    // height of the box
    int height;

    void print()
    {
        std::cout << x << " " << y << " " << width << " " << height << std::endl;
    }
 
};

ROI roi;

void roiCallback(const pal_detection_msgs::Detections2d::ConstPtr& msg)
{

  int duzina = sizeof(msg->detections);
  std::cout << duzina << std::endl;  

  for(int i = 0; i < duzina; i++)
  {
    roi.x = msg->detections[i].x;
    roi.y = msg->detections[i].y;
    roi.width = msg->detections[i].width;
    roi.height = msg->detections[i].height;

    roi.print();
  }
}

void depthCallback(const sensor_msgs::Image::ConstPtr& msg)
{
  ROS_INFO("dosla slika");
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "depth_listener");

  ros::NodeHandle n;

  ros::Subscriber roi_sub = n.subscribe("/person_detector/detections", 1000, roiCallback);

  ros::Subscriber depth_sub = n.subscribe("/xtion/depth_registered/image_raw", 1000, depthCallback);

  ros::spin();

  return 0;
}