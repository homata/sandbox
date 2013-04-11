Python & Django
-----------------
* [Djangoチュートリアル（前編）](http://codezine.jp/article/detail/4065)
* [Djangoチュートリアル（後編）](http://codezine.jp/article/detail/4264)

* [Djangoチュートリアルで"CSRF verification failed. Request aborted.](http://blog.w32.jp/2012/08/djangocsrf-verification-failed-request.html)
* [Djangoチュートリアル　エラーばっかり so may error of CSRF](http://suganoo.blogspot.jp/2013/01/django.html)
* [Djangoチュートリアル後編をやってみる](http://blog.livedoor.jp/ichsod/archives/1674798.html)


$ django-admin.py startproject ecsite
$ cd ./ecsite

$ manage.py runserver
$ manage.py syncdb

$ cd ./ecsite/ecsite
$ manage.py startapp itempage
$ manage.py syncdb
Would you like to create one now? (yes/no): yes
Username (leave blank to use 'homata'): admin
Email address: op.homata@gmail.com
Password: admin123
Password (again): admin123
Superuser created successfully.
Installing custom SQL ...
Installing indexes ...
Installed 0 object(s) from 0 fixture(s)


$ ./manage.py shell

    >>> from ecsite.itempage.models import Item
    >>> item = Item()
    >>> item.item_code='item-00001'
    >>> item.item_name='item1'
    >>> item.price=1000
    >>> item.save()
    >>> exit()

$ sqlite3 ecsite.sqlite
sqlite> select * from Item;
1|item-00001|item1|1000|
sqlite> .exit


