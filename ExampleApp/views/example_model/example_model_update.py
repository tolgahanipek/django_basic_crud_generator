from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from ExampleApp.models import ExampleModel

class ExampleModelUpdateView(UpdateView):
    model = ExampleModel
    template_name = "example_model/example_model_update.html"
    
     fields = '__all__'
    
     success_url = reverse_lazy('example_model_list')
    