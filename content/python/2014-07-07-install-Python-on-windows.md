Title: 在 Windows 下搭建 Python Web开发环境
Date: 2014-07-07 21:00
Category: Python
Tags: Python, Windows
comments: true
Slug: install-python-on-windows-1

本文将介绍如何在 Windows 系统下面安装和设置 Python Web开发环境，主要包括以下几个方面：
Python + Distribute + pip + virtualenv + virtualenvwrapper-win

## 安装 Python
* 到[Python官网](https://www.python.org/downloads/)下载 Python 安装程序，目前 Python 2.x 版本使用的最多，
我们这里也安装 Python 2.x版本，目前最新的是2.8
根据你自己的系统选择相对应的版本，由于我的系统是 Windows8.1 64位，所以选择64位版本的``Windows X86-64 MSI Installer (2.7.8)``。
在安装Python程序的时候选择默认安装即可。
安装完成后在 CMD 命令提示符下输入``python``，如果提示不是内部或者外部命令，表示环境变量还没有设置好。

* 新建环境变量,变量名为``path``，值为``C:\Python27;C:\Python27\Scripts``
如果选择新建系统环境变量，表示这台电脑上的所有用户都生效，
如果选择新建用户环境变量，则只对当前用户生效。

{% img /images/2014/PythonWindowsEnvironmentVariables.png 300 400 %}

## 安装 distribute / pip
* 首先下载[distribut_setup.py](http://python-distribute.org/distribute_setup.py)文件，
通过``python distribut_setup.py``安装，安装完成后就可以使用``easy_install``命令安装 Packages 了。
* 下载[get-pip.py](http://pip.readthedocs.org/en/latest/installing.html#install-pip)文件，在 CMD 命令提示符下输入``python get-pip.py``安装，
安装完成后就可以使用``pip install``命令安装 Packages 了。

## 安装 virtualenv / virtualenvwrapper-win
virtualenv 和 virtualenvwrapper-win 都可以用来创建虚拟环境，但是virtualenvwrapper-win可以用来管理多个虚拟环境。
* 安装 virtualenv：在 CMD 命令提示符下输入``pip install virtualenv``即可。
安装完成后，我们就可以在 CMD 命令提示符下使用``virtualenv ENV``来创建ENV这个虚拟环境了。
进入虚拟环境：``.\ENV\Script\activate``，推出虚拟环境：``.\ENV\Script\deactivate``
* 安装virtualenvwrapper-win：在 CMD 命令提示符下输入``pip install virtualenv-win``即可。
新建环境变量``WORKON``，值为``%USERPROFILE%\Envs``
创建虚拟环境：``mkvirtualenv ENV``，推出虚拟环境则直接输入``deactivate``即可。
进入虚拟环境：``WORKON ENV``

## SSH
PUTTY 和 Bitvise SSH Client

## IDE