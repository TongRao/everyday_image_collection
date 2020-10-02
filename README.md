Everyday Image Collection
=====
### **注意：本项目需要用到IOS端python集成开发环境Pythonista，此app为付费买断制app**

# 1. 介绍
由于最近在学习深度学习以及计算机视觉，突发奇想想要写一个在移动端也能随时拍照并对照片进行标注、简单预处理的小程序，正好之前买的Pythonista可以派上用场，搭配苹果的快捷指令app后用起来还算方便，由于Pythonista目前只在IOS端上线，所以此项目仅能在iPhone/iPad上运行。

## 1.1 Pythonista简介
Pythonista是一款IOS端的python集成开发环境，具有多个针对IOS开发的第三方库，可以便捷的访问设备功能， 如剪贴板、照片
摄像头等等，同时内置常用python第三方库，如numpy、matplotlib、bs4等等，是一款非常强大的IOS端python开发软件，[详情可访问官网](http://omz-software.com/pythonista/)

## 1.2 项目文件夹简介
项目根目录：
>project_root
>>take_photo.py

>>photos
>>>idx.txt

>>>photo_file

photos文件夹用于保存照片，照片名字格式为“label_idx.jpg”， 其中label为用户输入的照片label，idx为同种label里该照片的编号


# 2. 使用
## 2.1 直接在Pythonista运行
* 拷贝或下载文件夹至设备
* 用pythonista打开并运行take_photo.py

## 2.2 使用快捷指令创建桌面app
* 用pythonista打开take_photo.py，点击右上角设置按钮（扳手）
* 选择Shortcuts
* 选择Pythonista URL
* 点击Copy URL拷贝链接
* 在快捷指令中搜索并添加“URL”指令，并将之前拷贝的URL粘贴进去
* 在快捷指令中搜索并添加“打开URL”指令
* 点击快捷指令名字旁边的“...”，根据需求设置app logo和名字，添加到主屏幕
