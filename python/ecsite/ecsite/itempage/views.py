# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from models import Item

#from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
#from django.core.context_processors import csrf
from django.template import RequestContext
from forms import ItemSearchForm
from cart import CartItem
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # 単位は秒。15分キャッシュする。
def item_page_display(request,item_id):
    # item_idに該当するオブジェクトを取得する
    #item = Item.objects.get(id=item_id)
    #try:
    #    item = Item.objects.get(id=item_id)
    #except Item.DoesNotExist:
    #    raise Http404
    item = get_object_or_404(Item,id=item_id)  #ショートカットを使用（データが存在しない場合404エラーが返る）

    # テンプレートを取得して、モデルの値とマージする
    #t = loader.get_template('page/item.html')
    #c = Context(
    #    {'item':item }
    #)
    ## HTTP Responseを返す。
    #return HttpResponse(t.render(c))
    return render_to_response('page/item.html',
                    RequestContext(request, {'item': item}))

def item_search(request):
    #c = {}
    #c.update(csrf(request))

    if request.method == 'POST':
        form = ItemSearchForm(request.POST)
        if form.is_valid():
            items = Item.objects.filter(item_name=form.cleaned_data['item_name'])
            return render_to_response('page/item_search.html',
                            RequestContext(request, {'form': form, 'items': items}))
    else:
        #検索フォームの初期表示
        form = ItemSearchForm()

    return render_to_response('page/item_search.html',
                    RequestContext(request, {'form': form}))

def do_cart(request):

    # hiddenのitem_idを取得しintに型変換
    item_id = int(request.POST['item_id'])
    item = Item.objects.get(id=item_id)

    # DBからItem情報を取得する。
    cart_item_list = request.session.get('cart_item_list',[])
    ci = CartItem()
    ci.item_id = item_id
    ci.item_code = item.item_code
    ci.item_name = item.item_name
    ci.price = item.price
    ci.buy_num = request.POST['buy_num']
    cart_item_list.append(ci)
    request.session['cart_item_list'] = cart_item_list

    return render_to_response('page/cart_item_list.html',
                    RequestContext(request, {'cart_item_list': cart_item_list}))
