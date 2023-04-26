# gesture-recognition
后续会通过手势控制小车运动，这个后面在写。
本项目复现了YouTube上基于关键点的检测，后续还会加入用深度学习的方法。
关键点检测的方法直接放入了point-re文件夹中。
安装好相应的库就可以用了。（这个会点python的都会）特别说明，python的环境为python3。
使用`python3 FingerCounter.py`即可展示效果。具体效果如下：
https://www.bilibili.com/video/BV1sU4y1Z7ZG?spm_id_from=333.999.0.0   
### 2023.4.26   
加入了小车底盘代码arduino+L298N，摄像头从小车读图片（C++）出来后（因为jetson nano装的jepack4.6版本，且为U盘启动，Python代码打不开摄像头）   
读出图片后通过ROS发给python做处理识别。最后发出速度，C++接收后通过串口通信使小车运动。
