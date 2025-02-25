#!/usr/bin/env python3

import sys
import rclpy

from ariac_gazebo.environment_startup import EnvironmentStartup

def main():
    rclpy.init()

    startup_node = EnvironmentStartup()

    # Read trial configuration
    startup_node.trial_config = startup_node.read_yaml(sys.argv[1])

    # Read user configuration
    startup_node.user_config = startup_node.read_yaml(sys.argv[2])

    # Spawn robots
    startup_node.spawn_robots()

    # Spawn sensors
    startup_node.spawn_sensors()

    # Spawn parts in bins
    startup_node.spawn_bin_parts()

    # Spawn kit trays
    startup_node.spawn_kit_trays()

    # Spawn trays and parts on AGVs
    startup_node.spawn_parts_on_agvs()

    startup_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()