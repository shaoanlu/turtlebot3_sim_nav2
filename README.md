## About
This is a toy project that executes a ROS2 program w/ Gazebo and Nav2, while aiming for **minimum installation effort required**.

## Usage
1. Open WSL window
2. cd to this repo
3. docker compose up --build

## Result
A Gazebo window and a RViz window showing the SLAM visualizations.

## Problems encountered
### 1. Gazebo window not showing up (but a black box shown) after `ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py` 
### Sol.
In docker compose yaml, add the following config
```yaml
    environment:
      # Needed to define a TurtleBot3 model type
      - TURTLEBOT3_MODEL=burger
      # Allows graphical programs in the container.
      - DISPLAY=${DISPLAY}
      - QT_X11_NO_MITSHM=1
      - NVIDIA_DRIVER_CAPABILITIES=all
      - GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models
    volumes:
      # Allows graphical programs in the container.
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
      - ${XAUTHORITY:-$HOME/.Xauthority}:/root/.Xauthority
```
and source gazebo setup file
```yaml
    command: >
      bash -c "source /opt/ros/humble/setup.bash &&
               source /usr/share/gazebo/setup.bash &&
               ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py"
```