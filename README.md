# Mapping_ROS
Mapping_ROS
- OS : Ubuntu 18.04
- ROS : Melodic
- Map generator : SLAM-Gmapping
- Lidar : YDLIDAR X2
- IMU : MPU6050, HC-020K DC motor Encoder     
      
###
## 1. SLAM-Gmapping  
#### Simple Download
~~~
sudo apt-get install ros-melodic-slam-gmapping
~~~
or    
~~~
cd ~/catkin_ws/src/
git clone https://github.com/ros-perception/openslam_gmapping
git clone https://github.com/ros-perception/slam_gmapping.git
git clone https://github.com/ros-planning/navigation.git
git clone https://github.com/ros/geometry2.git
git clone https://github.com/ros-planning/navigation_msgs.git
cd ..
catkin_make
~~~
#### Useage
Required topic
> /scan /odom /tf       
Usage
~~~
rosrun mapping slam_gmapping
~~~
Output      
      


###
## 2. AMCL

###
## 3. Navigation Stack (move_base)



