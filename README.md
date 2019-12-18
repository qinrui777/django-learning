# jdango-learning
learning django, make a code record

[![python-version]][python]

---
|   Source    |
|:------------------|
|  Full-Featured Web App -> https://www.youtube.com/watch?v=UmljXZIypDc|
| Code source -> https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog|


### Env:
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
