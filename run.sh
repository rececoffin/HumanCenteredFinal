roslaunch turtlebot_bringup minimal.launch
roslaunch turtlebot_navigation amcl_demo.launch map_file:=~/Documents/HumanCenteredFinal/my_map.yaml
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
