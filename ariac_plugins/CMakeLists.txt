cmake_minimum_required(VERSION 3.8)
project(ariac_plugins)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(gazebo_msgs REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(rclcpp REQUIRED)
find_package(ariac_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)

link_directories(${gazebo_dev_LIBRARY_DIRS})

# Vacuum Gripper
add_library(vacuum_gripper SHARED
  src/vacuum_gripper.cpp
)
target_include_directories(vacuum_gripper PUBLIC include)
ament_target_dependencies(vacuum_gripper
  "gazebo_ros"
  "ariac_msgs"
)
ament_export_libraries(vacuum_gripper)

# Conveyor Belt Plugin
add_library(conveyor_belt_plugin SHARED
  src/conveyor_belt_plugin.cpp
)
target_include_directories(conveyor_belt_plugin PUBLIC include)
ament_target_dependencies(conveyor_belt_plugin
  "gazebo_ros"
  "ariac_msgs"
)
ament_export_libraries(conveyor_belt_plugin)

# AGV Plugin
add_library(agv_plugin SHARED
  src/agv_plugin.cpp
)
target_include_directories(agv_plugin PUBLIC include)
ament_target_dependencies(agv_plugin
  "gazebo_ros"
  "ariac_msgs"
)
ament_export_libraries(agv_plugin)

# Gripper Change Plugin
add_library(gripper_change_plugin SHARED
  src/gripper_change_plugin.cpp
)
target_include_directories(gripper_change_plugin PUBLIC include)
ament_target_dependencies(gripper_change_plugin
  "gazebo_ros"
  "ariac_msgs"
)
ament_export_libraries(gripper_change_plugin)

# Disable Shadows Plugin
add_library(disable_shadows_plugin SHARED
  src/disable_shadows_plugin.cpp
)
target_include_directories(disable_shadows_plugin PUBLIC include)
ament_target_dependencies(disable_shadows_plugin
  "gazebo_ros"
)
ament_export_libraries(disable_shadows_plugin)

ament_package()

install(DIRECTORY include/
        DESTINATION include)

install(TARGETS
    vacuum_gripper
    conveyor_belt_plugin
    agv_plugin
    gripper_change_plugin
    disable_shadows_plugin
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin)

# install(DIRECTORY models
#   DESTINATION share/${PROJECT_NAME}/
# )