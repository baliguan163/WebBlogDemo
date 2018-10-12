# WebBlogDemo
基于django的web blog app


django-admin startproject WebBlogDemo   # 创建WebBlogDemo项目
cd WebBlogDemo        # 切换到mysite目录
python manage.py startapp blog   #创建blog应用


 项目目录介绍:
--------
manage.py ： Django项目里面的工具，通过它可以调用django shell和数据库等。
MyTest/
| ---  settings.py ： 包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
| ---  urls.py ： 负责把URL模式映射到应用程序。
| --- wsgi.py :  用于项目部署。

blog /
| --- admin.py  :  django 自带admin后面管理，将models.py 中表映射到后台。
| --- apps.py :  blog 应用的相关配置。
| --- models.py  : Django 自带的ORM，用于设计数据库表。
| --- tests.py  :  用于编写Django单元测试。
| --- veiws.py ：视图文件，用于编写功能的主要处理逻辑。
