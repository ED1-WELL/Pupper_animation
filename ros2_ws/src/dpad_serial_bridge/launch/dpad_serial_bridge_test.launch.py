"""Standalone test launch: joy_linux_node + dpad_serial_bridge_node only.

Brings up just the two nodes needed to bench-test the D-pad -> Arduino bridge, without
the rest of the robot stack (no controllers armed, no actuators powered). Useful for
repeated manual testing during development; the full `neural_controller` launch.py
starts dpad_serial_bridge_node as part of the complete robot stack for normal operation.

Usage:
    ros2 launch dpad_serial_bridge dpad_serial_bridge_test.launch.py
"""

from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterFile
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    node_parameters = ParameterFile(
        PathJoinSubstitution([FindPackageShare("neural_controller"), "launch", "config.yaml"]),
        allow_substs=True,
    )

    joy_linux_node = Node(
        package="joy_linux",
        executable="joy_linux_node",
        parameters=[node_parameters],
        output="both",
        name="joy_linux_node",
    )

    dpad_serial_bridge_node = Node(
        package="dpad_serial_bridge",
        executable="dpad_serial_bridge_node",
        parameters=[node_parameters],
        output="both",
        name="dpad_serial_bridge",
    )

    return LaunchDescription([joy_linux_node, dpad_serial_bridge_node])
