from django.views.generic import TemplateView



class DeviceView(TemplateView):
    template_name = "device/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "DeviceView"
        return context