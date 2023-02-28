#include<ros/ros.h>		// include ros.h file

int main(int argc, char** argv)
{
  ros::init(argc, argv, "Hello_cpp_node") ;	// initial the node
  ros::NodeHandle handler;			// node's handler
  // ROS_INFO("Hello World!") ;			// print Hello World!

  while(ros::ok())
  {
    ROS_INFO("Hello World!") ;
    ros::Duration(1).sleep();
  }


}
