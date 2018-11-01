# python_web_blog
基于django的web blog app


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


django-admin startproject blog   # 创建blog项目
cd blog        # 切换到mysite目录
python manage.py startapp myadmin   #创建myadmin应用app

python manage.py makemigrations blog
python manage.py migrate blog


创建一个超级用户，用来登陆后台管理
python manage.py createsuperuser
python manage.py runserver

http://127.0.0.1:8000/admin/


python manage.py makemigrations这个命令是记录我们对models.py的所有改动，
并且将这个改动迁移到migrations这个文件下生成一个文件例如：0001文件，如果你接
下来还要进行改动的话可能生成就是另外一个文件不一定都是0001文件，但是这个命令并
没有作用到数据库，这个刚刚我们在上面的操作过程之后已经看到了，而当我们执行
python manage.py migrate 命令时  这条命令的主要作用就是把这些改动作用到
数据库也就是执行migrations里面新改动的迁移文件更新数据库，比如创建数据表，
或者增加字段属性

另外一个需要注意的是这两个命令默认情况下是作用于全局，也就是对所有最新更改的
models或者migrations下面的迁移文件进行对应的操作，如果要想仅仅对部分app进
行作用的话  则执行如下命令：

python manage.py makemigrations appname,
python manage.py migrate appname,

如果要想精确到某一个迁移文件则可以使用：

python manage.py migrate appname 文件名

