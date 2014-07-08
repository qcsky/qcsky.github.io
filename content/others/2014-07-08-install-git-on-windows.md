Title: 在 Windows 下安装 Git for Windows
Date: 2014-07-08 21:00
Category: Others
Tags: Git, Windows
comments: true
Slug: install-Git-on-windows

## 下载安装 Git for Windows
首先到[http://msysgit.github.io/ ](http://msysgit.github.io/ )官网下载安装文件，目前的版本是 1.9.4。
安装过程比较简单，有几个地方需要注意一下，其他的都可以安装默认设置安装即可。
* 第一个是选择组建，建议取消勾选 **Window Explorer integration** 这个选项

* 第二个是设置环境变量，对于不太熟悉 Bash 的朋友建议选择 **Run Git form the Windows Command Prompt**。

安装完成后直接打开 CMD 命令提示符，输入``git --version``查看 Git 的版本号。

## 设置 Git
``Git config``命令的``--global``参数是表示这台机器上所有的 Git 仓库都会使用设置配置
* 设置用户名 ``git config --global user.name "Your Name"``
* 设置邮箱``git config --global user.email "youemail@example.com"``
* 创建 SSH KEY ``ssh-keygen -t -rsa -C "youremail@example.com"``会在 ``C:\Users\<username>\.ssh`` 创建目录。

