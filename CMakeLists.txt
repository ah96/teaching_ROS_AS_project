cmake_minimum_required(VERSION 3.0.2)
project(my_simulation)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  pal_detection_msgs
  cv_bridge
  image_transport
)

find_package(OpenCV REQUIRED)

catkin_package(
  CATKIN_DEPENDS pal_detection_msgs roscpp image_transport cv_bridge
)

include_directories(SYSTEM ${catkin_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS})

foreach(dir launch worlds)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

install(PROGRAMS scripts/tuck_arm.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

add_executable(detect_person src/detect_person.cpp)
target_link_libraries(detect_person ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
