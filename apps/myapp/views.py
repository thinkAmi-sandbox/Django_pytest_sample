from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .model_forms import ItemModelForm
from .models import Item

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemModelForm
    
    def get_success_url(self):
        return reverse('my:item-detail', args=(self.object.id,))
        
        
class ItemDetailView(DetailView):
    model = Item