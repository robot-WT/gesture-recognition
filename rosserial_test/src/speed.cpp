#include<ros/ros.h>
#include<geometry_msgs/Twist.h>
#include<rosserial_test/SerialPort.h>
using namespace std;

struct speed {
        float x = 0.0;
        float y = 0.0;
        float z = 0.0;
}sp;

unsigned char speed_send[12];
void send_speed(const geometry_msgs::Twist::ConstPtr &speed_msg)
{
        sp.x = speed_msg->linear.x;
        sp.y = speed_msg->linear.y;
        sp.z = speed_msg->angular.z;

        memcpy(speed_send, &sp, 12);

        cout<<"speed_vx = "<<speed_msg->linear.x<<endl;
        //根据前面制定的发送贫频率自动休眠 休眠时间 = 1/频率；
}

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "SerialPort");
    ros::NodeHandle nh;
    geometry_msgs::Twist speed_msg;
    ros::Subscriber speed_sub = nh.subscribe<geometry_msgs::Twist>("/cmd_vel",10, send_speed);
    //串口初始化相关
    SerialPort w;
    bool flag_s = w.open("/dev/ttyUSB0", 9600, 0, 8, 1);
    cout<<"flag_s: "<<flag_s<<endl;
    if(!flag_s)
    {
        ROS_WARN("open serial port failed...");
        return 0;
    }
    //逻辑(一秒10次)
    ros::Rate r(10);
    unsigned char ac = 'n';
    //节点不死
    while (ros::ok())
    {
        if (sp.x>0.1 && sp.z==0)
        {
            ac = '0';
        }
        else if (sp.x<-0.1 && sp.z == 0)
        {
            ac = '1';
        }
        else if (sp.z<-0.05&& sp.x==0)
        {
            ac = '2';
        }
        else if (sp.z>0.05&& sp.x==0)
        {
            ac = '3';
        }
        else
        {
            ac = 'n';
        }
        int count_send =  w.send(&ac, sizeof(unsigned char));
        r.sleep();

        ros::spinOnce();
    }


    return 0;
}
