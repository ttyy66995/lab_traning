# MySQL
### 語法的選擇
Django ORM 物件-資料庫關聯操作
* 最符合Django框架設計屬性(MTV架構)
* 需多學簡單的base on python ORM operation語法

以python下MySQL 語法
* 速度與效能最佳，因為是直接下SQL語法
* 需另外學SQL語法


###  一般常用的套路
![](https://i.imgur.com/MkwFaap.png)


### 修改 settings.py
![](https://i.imgur.com/IDjauXm.png)

### 將資料表上傳至MySQL
利用圖形化介面：140.116.214.130/phpmyadmin
將資料表上傳至Database
* 記得設定主鍵(Primary key)

### 讓 Models.py 順利吃到資料表
於Linux terminal執行：python manage.py inspectdb > {app}/models.py

執行完後的{app}/models.py
![](https://i.imgur.com/82wwxaN.png)

### views.py
import資料表
![](https://i.imgur.com/xWpn26e.png)

於主程式內利用ORM語法撈資料
![](https://i.imgur.com/LnmHESc.png)


### Django ORM methond – ORM一些語法介紹
* Objects 是管理器，回傳回Queryset
* Stock_name_all = StockName.objects.all() #將此物件全部讀入Stock_name_all variable
* Stock_name_all = read_frame(Stock_name_all) #轉成dataframe(不建議)
* Want = StockName.objects.get(code='2330') #取出一列資料
* Want.{othercolumn}   #呼叫該列資料的其他行
* Filtered = StockName.objects.filter(col1 > 50, col2 <80, col3 ='name') #多重條件過濾查詢

更多的請自行上網查詢