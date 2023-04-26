#include<ros/ros.h>
#include<geometry_msgs/Twist.h>
#include<rosserial_test/speed.h>
using namespace std;

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "driver_to_cmd");
    ros::NodeHandle nh;
    ros::Rate r(1);
    rosserial_test::speed vel;
    vel.linear_x =1.0;
    vel.linear_y=2.0;
    vel.angular_z=0.6;
    ros::Publisher cmd_pub = nh.advertise<rosserial_test::speed>("/cmd_vel",  10);
    while (ros::ok())
    {
        cmd_pub.publish(vel);
    }
    



    return 0;
}