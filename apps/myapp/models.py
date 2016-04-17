from django.db import models
from django.core.exceptions import ValidationError

def validate_min_len(value):
    if len(value) < 3:
        raise ValidationError(
            ('Nameの値 {} は短すぎます'.format(value)),
            params={'value': value},
        )
    
def validate_zero_price(value):
    if value == 0:
        raise ValidationError(
            ('unit_priceにはゼロを設定できません'),
            params={'value': value},
        )


class Item(models.Model):
    name = models.CharField('Name',
                            max_length=255,
                            validators=[validate_min_len])
    unit_price = models.DecimalField('UnitPrice',
                                     max_digits=10,
                                     decimal_places=0,
                                     validators=[validate_zero_price])