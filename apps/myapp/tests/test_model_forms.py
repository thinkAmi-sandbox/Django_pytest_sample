from django.test import TestCase

from apps.myapp.model_forms import ItemModelForm

class Test_ItemModelFormまわり(TestCase):
    def test_form_onlyに値がない場合_エラー(self):
        form = ItemModelForm({'form_only': '',
                              'name': 'test',
                              'unit_price': 100})
        assert form.is_valid() == False
        
    def test_form_onlyにアルファベット以外がある場合_エラー(self):
        form = ItemModelForm({'form_only': '123',
                              'name': 'test',
                              'unit_price': 100})
        assert form.is_valid() == False
        
    def test_form_onlyにアルファベットだけの場合_エラーとならない(self):
        form = ItemModelForm({'form_only': 'abc',
                              'name': 'test',
                              'unit_price': 100})
        assert form.is_valid()
