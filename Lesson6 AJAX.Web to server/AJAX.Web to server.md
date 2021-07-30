# AJAX、Web to server

### Form與AJAX的差別

#### Form
![](https://i.imgur.com/zEFIFgO.png)

#### AJAX
![](https://i.imgur.com/qLIMFtV.png)


### AJAX操作流程
![](https://i.imgur.com/XZ7iggP.png)

* 詳細請見範例Code
* <備註> 清除快取快捷鍵：Shift + Ctrl + R

### Web to server
1. 告知管理員幫你寫配置檔
2. 建立新的虛擬環境"djvenv" (一定要叫這名字，不然配置會有問題)
3. pip install Django==1.11.1
4. 創建Django資料夾並startproject {user}_project (一定要叫這名字，不然配置會有問題)
5. 建立你的APP(跟本地端一樣) 並將static/、templates/、views.py、urls.py移過來
6. 修改 settings.py
* ALLOWED_HOSTS=["{ip}"]
* INSTALLED_APPS 確認
* MIDDLEWARE把第四行‘django.middleware.csrf.CsrfViewMiddleware’註解掉
* ROOT_URLCONF= ‘{user}_project.urls’
* TEMPLATES確認
* WSGI_APPLICATION= ‘{user}_project.wsgi.application’


* DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME’: {user}_database’,
    ‘USER’: ‘{user}',
    'PASSWORD': '624001479',
    'HOST': 'localhost',
    'PORT': '3306',
    'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        }
    }
* STATIC_URL = '/{user}_static/'
* STATICFILES_DIRS = [os.path.join(BASE_DIR, "static",]

7. 修改html、views.py、js等的路徑

8. 除錯
* less /var/log/apache2/error.log 最底部  (若權限被拒要請管理員開)
* 瀏覽器開F12開發者工具找錯誤

9. 完成



