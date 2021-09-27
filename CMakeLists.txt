cmake_minimum_required(VERSION 3.0.2)
project(my_simulation)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  pal_detection_msgs
)

catkin_package(
  CATKIN_DEPENDS pal_detection_msgs roscpp
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

foreach(dir launch worlds)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

install(PROGRAMS scripts/tuck_arm.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

add_executable(get_depth_of_person src/get_depth_of_person.cpp)
target_link_libraries(get_depth_of_person ${catkin_LIBRARIES})
#add_dependencies(talker beginner_tutorials_generate_messages_cpp)
