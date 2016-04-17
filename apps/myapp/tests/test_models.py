import pytest
from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.myapp.models import Item

class Test_Itemモデルまわり(TestCase):
    def test_nameが短すぎる場合_エラー(self):
        with pytest.raises(ValidationError) as excinfo:
            model = Item(name='a'*2, unit_price=100)
            model.full_clean()
        # ValidationErrorのエラーメッセージは`messages`に設定される
        # https://github.com/django/django/blob/8958170755b37ce346ae5257c1000bd936faa3b0/django/core/exceptions.py#L143
        assert 'Nameの値 aa は短すぎます' in excinfo.value.messages
            
    @pytest.mark.parametrize(['input',],[('a'*3), ('a'*255),])
    # parametrizeを使う場合、selfは引数として受け取らない模様
    def test_nameが正常な場合_エラーとならない(input):
        model = Item(name=input, unit_price=100)
        try:
            model.full_clean()
        except:
            pytest.fail()
            
    def test_nameが長すぎる場合_エラー(self):
        # 例外メッセージはデフォルトのものを使うので、メッセージ内容まではチェックしない
        with pytest.raises(ValidationError):
            model = Item(name='1'*256, unit_price=100)
            model.full_clean()
        
    def test_unit_priceがゼロの場合_エラー(self):
        with pytest.raises(ValidationError) as excinfo:
            model = Item(name='abc', unit_price=0)
            model.full_clean()
        assert 'unit_priceにはゼロを設定できません' in excinfo.value.messages
        
    def test_unit_priceが正常な場合_エラーとならない(self):
        model = Item(name='abc', unit_price=10**9)
        try:
            model.full_clean()
        except:
            pytest.fail()
            
    def test_unit_priceが長すぎる場合_エラー(self):
        with pytest.raises(ValidationError):
            model = Item(name='abc', unit_price=10**10)
            model.full_clean()


    def test_エラーがない場合_データが保存される(self):
        model = Item(name='abc', unit_price=100)
        model.save()
        
        saved = Item.objects.all()
        actual = saved[0]
        
        assert saved.count() == 1
        assert actual.name == 'abc'
        assert actual.unit_price == 100