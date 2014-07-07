Title: 在Windows系统上安装Pelican-1
Date: 2014-07-06 21:00
Category: Python
Tags: Python, Pelican, Git, Windows
comments: true
Slug: install-Pelican-on-windows-1

## 介绍
这篇文章主要介绍一下如何在Windows系统上安装设置Pelican并发布到[Github](http://github.com)。
目前在Github上比较流行的静态网站程序是`Octopress`和`Pelican`,本站就是使用`Pelican`搭建的。
因为最近在学习`Python`，而`Pelican`又是以`Python`语言 编写的，所以选择了`Pelican`。
在下面的文章中我们将一步一步教你如何在 Windows 系统下搭建一个静态 Pelican Blog, 并发布到 Github 上。
## 安装设置虚拟环境
* 利用virtuaenv创建虚拟环境： 
  {% virtualenv VEnv  %}
笔者的虚拟环境是在`D:\Project\Python\VEnv`这个目录，
`cmd`到当前目录下，使用`.\VEnv\Scripts\activate`来启动虚拟环境，前面有个`(VEnv)`表示启动虚拟环境成功。
	
		D:\Project\Python>.\VEnv\Scripts\activate
		(VEnv) D:\Project\Python>

* 安装设置 Pelican 和 Markdown
安装 Pelican：进入到虚拟环境后我们直接使用`pip install pelican`。
安装 Markdown：如果我们要用到`Markdown`来写文章的话就需要安装，直接使用`pip install markdown`
接着我们在创建一个名为 `qcsky.github.io`的文件夹，这个文件夹可以随便起名，
笔者文件夹的路径为`D:\Project\Python\qcsky.github.io`,
我们在虚拟环境的cmd窗口里面进入到qcsky.github.io这个目录,执行`pelican-quickstart`命令，按照提示一步一步设置完成，
这些以后都可以在`pelicanconf.py`这个文件里面修改。

		(VEnv) D:\Project\Python\qcsky.github.io>pelican-quickstart
		Welcome to pelican-quickstart v3.4.0.

		This script will help you create a new Pelican-based website.

		Please answer the following questions so this script can generate the files
		needed by Pelican.

		> Where do you want to create your new web site? [.]
		> What will be the title of this web site? qcsky's blog
		> Who will be the author of this web site? qcsky
		> What will be the default language of this web site? [en]
		> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
		> What is your URL prefix? (see above example; no trailing slash) http://qcsky.github.io
		> Do you want to enable article pagination? (Y/n)
		> How many articles per page do you want? [10]
		> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
		> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
		> Do you want to upload your website using FTP? (y/N)
		> Do you want to upload your website using SSH? (y/N)
		> Do you want to upload your website using Dropbox? (y/N)
		> Do you want to upload your website using S3? (y/N)
		> Do you want to upload your website using Rackspace Cloud Files? (y/N)
		> Do you want to upload your website using GitHub Pages? (y/N)
		Done. Your new project is available at D:\Project\Python\qcsky.github.io

执行完成后，你的qcsky.github.io目录将会包括以下几个目录和文件：

		qcsky.github.io/
		├── content                # 存放输入的markdown或RST源文件
		├── output                 # 存放最终生成的静态博客
		├── fabfile.py			   # 发布
		├── develop_server.sh      # 测试服务器
		├── Makefile               # 管理博客的Makefile
		├── pelicanconf.py         # 配置文件
		└── publishconf.py         # 发布文件，可删除
* 用`Markdown`写文章
完成上面的 Blog 环境搭建后，可以使用你熟悉的编辑器创建一个以`.md`为后缀的文件，并把它保存到content目录。
Markdown文件的头部是必须的，具体的可以参考下官方文档
		Title: 文章标题
		Date: 创建时间
		Category: 文章分类
		Tags: 文章标签
		comments: true
		Slug: URL中该文章的链接地址
执行`pelican content -o output -s pelicanconf.py` 后在output目录生成静态 Blog 目录
	
		(VEnv) D:\Project\Python\qcsky.github.io>pelican content -o output -s pelicanconf.py
再执行以下命令启动测试服务器，

		cd D:/Project/Python/qcsky.github.io/output && python -m pelican.server
在浏览器中输入http://localhost:8000即可看到 Blog 效果

## 发布到Github
首先创建一个以你·Github用户名.github.io`的仓库，比如我的就是qcsky.github.io
然后到output目录，依次执行以下命令创建本地 Git 仓库，并推送到 Github 远端仓库。

		qcsky.github.io\output>git init
		qcsky.github.io\output>git add .
		qcsky.github.io\output>git commit -m "Initial"
		qcsky.github.io\output>git remote add origin https://github.com/qcsky/qcsky.github.io.git
		qcsky.github.io\output>git push master --force
现在你就可以通过http://yourusername.github.io来访问你的 Blog 了。