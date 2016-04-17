import pytest
from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.myapp.views import ItemCreateView, ItemDetailView
from apps.myapp.models import Item


class Test_POSTリクエストまわり(TestCase):
    def test_ItemCreateViewのOKパターン_followはTrue(self):
        response = self.client.post(reverse('my:item-creation'), 
                                    {
                                        'form_only': 'alphabet',
                                        'name': 'post_test',
                                        'unit_price': 100,
                                    }, 
                                    follow=True)
        # リダイレクトしているかどうか
        self.assertRedirects(response, reverse('my:item-detail', kwargs={'pk': 1}), status_code=302)
        
        # Viewまわり
        assert response.resolver_match.func.__name__ == ItemDetailView.as_view().__name__
        
        # テンプレートまわり
        assert response.context['object'].name == 'post_test'
        assert response.context['object'].unit_price == 100
        assert response.context['item'].unit_price == 100
        
        # データベースまわり
        actual = Item.objects.all()
        actual_item = actual[0]
        
        assert actual.count() == 1
        assert actual_item.name == 'post_test'
        assert actual_item.unit_price == 100
        
        
    def test_ItemCreateViewのバリデーションエラーパターン(self):
        response = self.client.post(reverse('my:item-creation'), 
                                    {
                                        'form_only': '1',
                                        'name': 'post_test',
                                        'unit_price': 100,
                                    })
        
        # 第二引数は、フォームのcontext名であることに注意
        # http://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django
        self.assertFormError(response, 'form', 'form_only', 'form_onlyの値 1 にアルファベット以外が含まれています')
        
        # オブジェクト名とかだと以下のエラーになる
        # from apps.myapp.model_forms import ItemModelForm
        # AssertionError: The form 'ItemModelForm' was not used to render the response
        # self.assertFormError(response, ItemModelForm.__name__, 'form_only', '1 is only alphabet')
        
        
        # Djangoでは、バリデーションエラーのステータスコードは200
        assert response.status_code == 200
        
        # Viewまわり
        assert response.resolver_match.func.__name__ == ItemCreateView.as_view().__name__
        
        # DBまわり
        assert Item.objects.all().count() == 0
        