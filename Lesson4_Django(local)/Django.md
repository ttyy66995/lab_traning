# Django

### 1.安裝
* 開啟Anaconda Prompt 
* pip install Django==1.11.1

### 2.建立專案
* 創建"Django"資料夾
* django-admin.py startproject **[name]**

### 3.建立APP
* 進入 **[name]**/資料夾
* python manage.py startapp **[appname]**

* 打開 **[name]**/**[name]**/settings.py，找到INSTALLED_APP,加入APP名字

![](https://i.imgur.com/490BYQK.png)

* 在 **[name]**/**[name]**/資料夾內修改 urls.py

![](https://i.imgur.com/CNpW0lJ.png)

### 4.建立templates
* 在 **[name]**/資料夾內創建"templates"資料夾
* 將自己的html檔放入templates資料夾內
* 在 **[name]**/**[name]**/settings.py 中的TEMPLATES內的DIR內加上
os.path.join(BASE_DIR, ‘templates’) 

![](https://i.imgur.com/f0hzC5j.png)

* 在APP資料夾內的 view.py 放函式

![](https://i.imgur.com/09cFfIy.png)

* 在APP資料夾內創建 urls.py

![](https://i.imgur.com/mKLBU9n.png)
> <備註>這邊使用進階結構管理:
> project的 urls.py 中只用來include APP的 urls.py
> project/project/urls.py
> app1/urls.py
> app2/urls.py

### 5.建立static
* 在 **[name]**/資料夾內創建"static"資料夾，裡面再創建靜態檔案資料夾:css,js,image
* 在 **[name]**/**[name]**/settings.py 中寫入
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]

![](https://i.imgur.com/yKqFtt8.png)

* 修改html檔，開頭寫上{% load staticfiles %}
* 並於<head></head>之間加入
.<link rel="stylesheet" href="{% static 'css/{filename}.css' %}">

![](https://i.imgur.com/jJzFYxj.png)

### 6.完成
* 回到 **[name]**/資料夾
* python manage.py runserver
* See 127.0.0.1:8000

