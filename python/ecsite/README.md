Python & Django
================

Python
----------
* [Python本家](http://www.python.org/)
* [Puthin Japan (PyJUG)](http://www.python.jp/)
* [Python入門](http://python.keicode.com/)

Django
----------
* [django本家](https://www.djangoproject.com/)
* [djangoproject.jp (日本のユーザコミュニティ)](http://djangoproject.jp)

* [Django Document 1.5](https://docs.djangoproject.com/en/1.5/)
* [Django ドキュメント](http://djangoproject.jp/doc/ja/1.0/)

ドキュメント
----------
* [Pythonの環境設定でむかついてる人はとりあえずこれをコピペで実行してください](http://ymotongpoo.hatenablog.com/entry/2012/10/18/144352)
* [Python Tips](http://www.gesource.jp/programming/python/index.html)
* [Djangoチュートリアル（前編）](http://codezine.jp/article/detail/4065)
* [Djangoチュートリアル（後編）](http://codezine.jp/article/detail/4264)
* [「Python×Django×AWS」によるモバイル向けソーシャルアプリ開発の裏側](http://codezine.jp/article/detail/5311)
    * 開発にはPythonと、
    * そのフレームワークである「Django」、
    * サービス管理はGit、
    * デプロイはCapistrano、
    * サービス運用はAmazon Web Services(AWS)を利用しているとのことです。

    * なお、同社の一般的なアプリの構成としては、
    * Amazon EC2側はロードバランサーが1〜2台、
    * アプリケーションサーバーが5〜20台、
    * ログ管理用のNFSサーバーが1台、
    * memcachedのキャッシュサーバーが1台、
    * Tokyo Tyrantのデータベースサーバーが2台で、
    * Amazon RDS側でMySQL 5.1のデータベースサーバーが1台  
    という組み合わせが使われているとのこと。
* [Perl, Python, Ruby比較](http://www.devsite.jankh.net/compppr.html#u9449bf1)

##### Djangoをインストールしたら最初にすること
* [その1(プロジェクト作成・サーバ設定・表示確認)](http://blog.layer8.sh/ja/2011/12/28/django%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%9F%E3%82%89%E6%9C%80%E5%88%9D%E3%81%AB%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8-%E3%81%9D%E3%81%AE%EF%BC%91%E3%83%97/)
* [その2(DB作成・接続・同期とadminモジュールの実装)](http://blog.layer8.sh/ja/2011/12/26/django%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%9F%E3%82%89%E6%9C%80%E5%88%9D%E3%81%AB%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8-%E3%81%9D%E3%81%AE%EF%BC%92db%E4%BD%9C/)

##### SQLite
* [SQLite](http://www.sqlite.org/)

##### CSRF対策
* [Djangoチュートリアルで"CSRF verification failed. Request aborted.](http://blog.w32.jp/2012/08/djangocsrf-verification-failed-request.html)
* [Djangoチュートリアル　エラーばっかり so may error of CSRF](http://suganoo.blogspot.jp/2013/01/django.html)
* [Djangoチュートリアル後編をやってみる](http://blog.livedoor.jp/ichsod/archives/1674798.html)

##### OAuth
* [pythonで署名付きリクエストを送る(2-legged OAuth)](http://taichino.com/programming/1057)


Memo
----------

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



