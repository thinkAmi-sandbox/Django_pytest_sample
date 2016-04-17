import pytest
from django.test import TestCase
from django.core.urlresolvers import resolve, Resolver404

from apps.myapp.views import ItemCreateView, ItemDetailView


class Test_URL解決まわり(TestCase):
    def test_存在しないURLの場_エラー(self):
        with pytest.raises(Resolver404):
            resolve('/mysite/not-exist')
        
    def test_商品登録のURLの場合_URL解決される(self):
        found = resolve('/mysite/create')
        assert found.func.__name__ == ItemCreateView.__name__
        
    def test_商品詳細のURLの場合_URL解決される(self):
        # DBにデータがないので404テンプレートが使われるけど、resolveされている
        found = resolve('/mysite/item/1/')
        assert found.func.__name__ == ItemDetailView.__name__