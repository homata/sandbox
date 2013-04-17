Python & Django
================

Python
----------
* [Python本家](http://www.python.org/)
* [Puthin Japan (PyJUG)](http://www.python.jp/)
* [Python入門](http://python.keicode.com/)

* [Python 2.7ja1 documentation](http://docs.python.jp/2/)
* [Python 言語リファレンス 2.7](http://docs.python.jp/2/reference/index.html#reference-index)
* [Python 標準ライブラリ 2.7](http://docs.python.jp/2/library/index.html)

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
* [Pythonの定番モジュール集](http://coreblog.org/ats/well-used-python-modules)
* [Python OpenSSL Manual](http://pythonhosted.org/pyOpenSSL/pyOpenSSL.html)

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

##### easy_install、setuptools、pip - パッケージ管理
* [easy_install、setuptools、pip - パッケージ管理](http://www.tomoyan.net/dokuwiki/python/easy_install)
* [pipの使い方](http://d.hatena.ne.jp/rudi/20110107/1294409385)
* [pipとvirtualenvがすごい便利だっと今日気付いた。](http://rokujyouhitoma.hatenablog.com/entry/20100928/1285685693)

Linux & Mac 編(ez_setup.pyの場合)  

1. ez_setup.py をダウンロード。  
    $ curl -O http://peak.telecommunity.com/dist/ez_setup.py
2. インストールする。  
    $ sudo python ez_setup.py
3. easy_install の動作確認をする。  
    $ easy_install --help
4. pip のインストールを行う。  
    $ sudo easy_install pip
5. pip を更新する場合  
    $ sudo easy_install -U pip
6. pip の動作確認をする。  
    $ pip --version

virtualenv
---------

* [virtualenv](http://www.virtualenv.org/en/latest/)
* [VIRTUALENV について](http://blog1.erp2py.com/2011/07/virtualenv.html)

    $ sudo apt-get install python-pip
    $ sudo pip install virtualenv

pip & Django
------------
    $ sudo pip install Django==1.5.1
    $ python
    Python 2.7.3 (default, Aug  1 2012, 05:16:07)
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import django
    >>>
    >>> django.VERSION
    (1, 5, 1, 'final', 0)
    >>> exit()


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


---------------------------------

メモ
====================

* [Python Module of the Week](http://ja.pymotw.com/2/)
* [logging – ステータス、エラー、その他の情報をログ出力する](http://ja.pymotw.com/2/logging/)


