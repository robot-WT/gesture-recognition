#include "rosserial_test/odom_req.h"

int main(int argc, char** argv )
{
    ros::init(argc, argv, "lino_base_node");
    LinoBase lino;
    ros::spin();
    return 0;
}