#include <ros/ros.h>
#include <pal_detection_msgs/Detections2d.h>
#include <pal_detection_msgs/Detection2d.h>
#include <sensor_msgs/Image.h>
#include <iostream>
#include <typeinfo>
#include <cv_bridge/cv_bridge.h>

bool isNaN(float num)
{
    return !(num == num);
}

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

void roiCallback(pal_detection_msgs::Detections2d msg) //const pal_detection_msgs::Detections2d::ConstPtr& msg
{

  std::cout << std::endl << "empty: " << msg.detections.empty() << std::endl;

  // if there are no persons detected
  if(msg.detections.empty() == true)
  {
    std::cout << "empty" << std::endl;

    roi.x = 0;
    roi.y = 0;
    roi.width = 0;
    roi.height = 0;

    roi.print();
  }
  else
  {
    std::cout << "non-empty" << std::endl;

    std::cout << "array size: " << sizeof(msg.detections) << std::endl;

    std::cout << "one array element size: " << sizeof(msg.detections[0]) << std::endl;

    std::cout << "pal_detection_msgs::Detections2d size: " << sizeof(pal_detection_msgs::Detections2d) << std::endl;

    std::cout << "pal_detection_msgs::Detection2d size: " << sizeof(pal_detection_msgs::Detection2d) << std::endl;
    
    /*
    for(int i = 0; i < 1; i++)
    {
      std::cout << "i: " << i << ", " << msg->detections[i].x << " " << msg->detections[i].y << " " << msg->detections[i].width << " " << msg->detections[i].height << std::endl;
    }
    */

    for(int i = 0; i < 1; i++)
    {
      if(msg.detections[i].x < 0 || msg.detections[i].x > 640 || msg.detections[i].y < 0 || msg.detections[i].x > 480
      || msg.detections[i].x+msg.detections[i].width > 640 || msg.detections[i].y+msg.detections[i].height > 480)
      {
        roi.x = 0;
        roi.y = 0;
        roi.width = 0;
        roi.height = 0;        
      }
      else
      {
        roi.x = msg.detections[i].x;
        roi.y = msg.detections[i].y;
        roi.width = msg.detections[i].width;
        roi.height = msg.detections[i].height;
      }

      roi.print();
    } 
  } 
}

void depthCallback(const sensor_msgs::Image::ConstPtr& msg)
{
  cv_bridge::CvImageConstPtr cvImgPtr;
  cvImgPtr = cv_bridge::toCvShare(msg);

  //std::cout << cvImgPtr->image.cols << " " << cvImgPtr->image.rows << " " << cvImgPtr->image.type() << std::endl;

  //std::cout << cvImgPtr->image.at<float>(300,300) << std::endl;

  ros::Time _imgTimeStamp = msg->header.stamp;

  //cv::Mat img(static_cast<int>(cvImgPtr->image.rows), static_cast<int>(cvImgPtr->image.cols), cvImgPtr->image.type());

  //cvImgPtr->image.copyTo(img);            

  depth_avg = 0.0;
  int num_samples = 0;
  depth_std_dev = 0.0;

  if(roi.y == 0 || roi.height == 0 || roi.x == 0 || roi.width == 0 || roi.y+roi.height > 480 || roi.x+roi.width > 640)
  {
    return;
  }

  //std::cout << roi.y << " " << roi.height << " " << roi.x << " " << roi.width << std::endl;

  for(int i = roi.y+1; i < roi.y + roi.height; i++)
  {
    for(int j = roi.x+1; j < roi.x + roi.width; j++)
    {
      //std::cout << i << " " << j << " " << cvImgPtr->image.at<float>(i, j) << std::endl;
      if(!isNaN(cvImgPtr->image.at<float>(i, j)))
      { 
        //std::cout << i << " " << j << " " << cvImgPtr->image.at<float>(i, j) << std::endl;
        depth_avg += cvImgPtr->image.at<float>(i, j);
        num_samples++;
      }
    }
  }

  depth_avg /= num_samples;
  std::cout << "depth_avg: " << depth_avg << std::endl;
  std::cout << "num_samples: " << num_samples << std::endl;               
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