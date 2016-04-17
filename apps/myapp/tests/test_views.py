from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from apps.myapp.views import ItemCreateView
from apps.myapp.models import Item

class Test_ItemCreateViewまわり(TestCase):
    def test_登録画面Viewが使われている_Client版(self):
        response = self.client.get(reverse('my:item-creation'))
        
        self.assertTemplateUsed(response, 'myapp/item_form.html')
        assert response.status_code == 200
        
        
    def test_登録画面Viewが使われている_RequestFactory版(self):
        request = RequestFactory().get(reverse('my:item-creation'))
        response = ItemCreateView.as_view()(request)
        
        # テンプレート名はlistで入ってるのでinを使って確認する
        # https://docs.djangoproject.com/ja/1.9/ref/template-response/#django.template.response.SimpleTemplateResponse
        assert 'myapp/item_form.html' in response.template_name
        assert response.status_code == 200 


    def test_詳細画面Viewが使われている_Client版(self):
        # データを登録しないと表示されないので、事前に登録しておく
        Item(name='abc', unit_price=100).save()
        response = self.client.get(reverse('my:item-detail', args=(1,)))
        
        self.assertTemplateUsed(response, 'myapp/item_detail.html')
        assert response.status_code == 200
        
        
    def test_詳細画面Viewが使われている_RequestFactory版(self):
        Item(name='abc', unit_price=100).save()
        request = RequestFactory().get(reverse('my:item-detail', args=(1,)))
        response = ItemCreateView.as_view()(request)
        
        assert 'myapp/item_form.html' in response.template_name
        assert response.status_code == 200