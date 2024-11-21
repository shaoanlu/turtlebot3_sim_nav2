# Use the official ROS2 Humble Desktop image
FROM osrf/ros:humble-desktop

# Install additional required packages
RUN apt-get update && apt-get install -y \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-turtlebot3-gazebo \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-turtlebot3-navigation2 \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# Set up TurtleBot3 model environment
ENV TURTLEBOT3_MODEL=burger

# Copy application scripts
WORKDIR /app
COPY scripts /app/scripts

# Add a default command to source ROS 2 setup and launch the application
CMD ["bash", "-c", "source /opt/ros/humble/setup.bash && source /usr/share/gazebo/setup.bash"]
