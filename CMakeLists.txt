cmake_minimum_required(VERSION 3.8)
project(kratos_atrijverma)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)

install(PROGRAMS
q1_hello.py
q1_subscriber.py
q2_s1.py
q2_s2.py
q4_clock.py
DESTINATION lib/${PROJECT_NAME}
)

rosidl_generate_interfaces(${PROJECT_NAME}
  "src/msg/Rover.msg"
  DEPENDENCIES geometry_msgs builtin_interfaces
)

ament_package()
