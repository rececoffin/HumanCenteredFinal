xterm -e "roslaunch turtlebot_bringup minimal.launch"
xterm -e "roslaunch turtlebot_navigation amcl_demo.launch map_file:=~/Documents/HumanCenteredFinal/my_map.yaml"
xterm -e "roslaunch turtlebot_rviz_launchers view_navigation.launch --screen"
