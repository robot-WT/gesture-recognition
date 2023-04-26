cmake_minimum_required(VERSION 3.0.2)
project(rosserial_test)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  geometry_msgs
  message_generation
  tf2
  tf2_ros
  nav_msgs
)


 add_message_files(
   FILES
   speed.msg
 )



## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)



catkin_package(
 # INCLUDE_DIRS include
  #LIBRARIES rosserial_test
  CATKIN_DEPENDS roscpp std_msgs message_runtime tf2 tf2_ros nav_msgs
  #DEPENDS system_lib
)

## Your package locations should be listed before other locations
include_directories(
include
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
 add_library(head
   include/rosserial_test/SerialPort.h
   src/SerialPort.cpp
 )
 add_library(odom
 include/rosserial_test/odom_req.h
 src/odom_req.cpp
)


 add_dependencies(head ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
 add_dependencies(odom ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

 add_executable(speed src/speed.cpp)
 add_executable(odom_req_node src/odom_req_node.cpp)

 add_dependencies(odom_req_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
 add_dependencies(speed ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
 target_link_libraries(head
   ${catkin_LIBRARIES}
 )
 target_link_libraries(odom
 ${catkin_LIBRARIES}
)

target_link_libraries(speed
  head
  ${catkin_LIBRARIES}
)
target_link_libraries(odom_req_node
  odom
  ${catkin_LIBRARIES}
)
add_executable(driver_to_cmd
  src/driver_to_cmd.cpp
)
target_link_libraries(driver_to_cmd
  ${catkin_LIBRARIES}
)