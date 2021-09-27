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

float depth_avg = 0.0, depth_std_dev = 0.0;

void roiCallback(const pal_detection_msgs::Detections2d::ConstPtr& msg)
{

  //int duzina = sizeof(msg->detections);
  //std::cout << duzina << std::endl;  

  for(int i = 0; i < 1; i++)
  {
    roi.x = msg->detections[i].x;
    roi.y = msg->detections[i].y;
    roi.width = msg->detections[i].width;
    roi.height = msg->detections[i].height;

    //roi.print();
  }
}

void depthCallback(const sensor_msgs::Image::ConstPtr& msg)
{
  ROS_INFO("dosla slika");

  int data_len = sizeof msg->data; // / sizeof msg->data[0];
  std::cout << "data_len: " << data_len << std::endl;

  data_len = sizeof msg->data[0]; // / sizeof msg->data[0];
  std::cout << "data[0]_len: " << data_len << std::endl;

  //std::cout << 'data[0]: ' << msg->data[0] << std::endl;
  std::cout << "msg->width: " << msg->width << std::endl;
  std::cout << "msg->height: " << msg->height << std::endl;
  std::cout << "msg->encoding: " << msg->encoding << std::endl;
  std::cout << "msg->step: " << msg->step << std::endl;

  int i = 0;
  for(i=0;i<1000000;i++)
  {
    int x = msg->data[i];
    std::cout << "data[" << std::to_string(i) << "]: " << x << std::endl;
  }
  std::cout << "i = " << i << std::endl;
  
  /*
  depth_avg = 0.0;
  depth_std_dev = 0.0;

  for(int i = roi.y; i <= roi.y + roi.height; i++)
  {
    for(int j = roi.x; i <= roi.x + roi.width; j++)
    {
      depth_avg += msg->data[i * 640 + j];
    }
  }

  depth_avg /= (roi.height * roi.width);
  std::cout << 'depth_avg: ' << depth_avg << std::endl;
  */
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