# jdango-learning
learning django, make a code record

[![python-version]][python]

---
|   Source    |
|:------------------|
|  Full-Featured Web App -> https://www.youtube.com/watch?v=UmljXZIypDc|
| Code source -> https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog|


### My Env/Requirements:
- Mac os
- sublime 3.2.2  (注意开启自动保存，tab键转换为空格,python对空格较严格)
- Python 3.7
- Django 3.0

---

#### 01_setup_env

```python
#use python3.7
~ python3 --version
Python 3.7.5

#install django
pip3 install django

#check django version,be sure >2.1
python3 -m django --version
```

**Starting development server**

`python manage.py runserver`

*可在浏览器访问*

- http://localhost:8000
- http://localhost:8000/admin/ (可访问，但暂时无法登陆)

#### 02_Applicatinos&Routes

**在root目录下，创建子app**  
`python manage.py startapp blog`

*output:*
```bash
tree
.
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── django_demo
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

#### 03_Templates

- 使用template
  - 1.在 blog目录下新建 templates/blog 目录
  - 2.jinja语法( for循环、if else判断）
  - 3.使用 base.html (block)

- 使用bootstrap
  - base.html中插入bootstrap [代码](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)

- 自定义`css`样式  
  - 新建静态文件目录 blog/static/blog/xxx.css
  - 提供的[snippets](https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog/snippets)

#### 04_admin_page

```bash
➜  python manage.py makemigrations
No changes detected
➜  python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
.....
➜  python manage.py createsuperuser
Username (leave blank to use 'ruqin'): admin
Email address: ruqin@thoughtworks.com
```

> http://localhost:8000/admin/ (admin/admin123)

####  05_Database&migrations

django has its own built-in ORM  
  - SQLite for development
  - Postgres for production

- create`Post`

```bash
# 有新增model时，需要用以下的命令将数据结构导入database中
➜   python manage.py makemigrations
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post

➜   python manage.py sqlmigrate blog 0001
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
➜  django_demo python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
```

```python
##通过shell交互方式操作python object对象
➜   python manage.py shell
Python 3.7.5 (default, Nov  1 2019, 02:16:38)
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
#导入Post User model
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: admin>]>
>>> User.objects.filter(username='admin')
<QuerySet [<User: admin>]>
>>> User.objects.first()       # 还有last()方法
<User: admin>
>>> user = User.objects.first()  #定义变量 user ,并赋值
>>> user.id
1
>>> Post.objects.all()
<QuerySet []>
>>> post_1 = Post(title='blog 1',content='First post content!',author=user)
>>> Post.objects.all()
<QuerySet []>
>>> post_1.save()    # 需要调用save() 方法，才生效
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>]>
# 在models.py 定义Post的 __str__方法，以便有返回值
# 然后执行exit()退出，重新进入交互模式

>>> post_2 = Post(title='blog 2',content='second post content',author=user)
>>> post_2.save()
>>> Post.objects.all()
<QuerySet [<Post: blog 1>, <Post: blog 2>]>
>>> post = Post.objects.first()
>>> post
<Post: blog 1>
>>> post.content
'First post content!'
>>> post.date_posted
datetime.datetime(2019, 12, 13, 6, 16, 22, 338009, tzinfo=<UTC>)
>>> post.author.email   #通过外键直接获取 user的email
'ruqin@thoughtworks.com'

>>> user.post_set.all()
<QuerySet [<Post: blog 1>, <Post: blog 2>]>
>>> user.post_set.create(title='blog 3',content='Third post content!')
<Post: blog 3>
```

- 替换之前的post 的dummy data `blog/views.py`
- 更改post日期格式 `blog/templates/home.html` ([python format date](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date))
- 将Post模型 注册到admin页面, 修改文件`blog/admin.py`

#### 06_User_registration
为了满足用户注册、登陆等功能，需要新建一个类似blog的子app
`python manage.py startapp users`

- 在 `django_demo/setting.py` 添加 `'users.apps.UsersConfig',`
- 在 `user/views.py` 创建 `register()` 方法 （直接利用UserCreationForm方法新建表单内容）
- 在目录 `users` 下新建目录 `templates/users`,然后新建文件 `register.html`，完善页面显示内容
- 在 `django_demo/urls.py` 中添加 `register` 路径, 打开路径 http://localhost:8000/register/ 测试下
- 在 `user/views.py` 中加入对 `request.method` 方法的判断，加入 `messages` 信息展示集成到 `base.html`中
> django内建的UserCreationForm能校验部分数据有效性
- 在注册页面添加email字段, 新建 `users/form.py `