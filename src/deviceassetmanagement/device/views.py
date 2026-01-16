from django.views.generic import TemplateView
from django.views.generic import ListView
from django.db.models import Q, Count
from .models import Device
from .models import DeviceType


class DeviceView(ListView):
    model = Device
    template_name = "device/index.html"
    context_object_name = "devices"
    paginate_by = 20
    
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related('device_type')
        q = self.request.GET.get('q', '').strip()
        condition_filter = self.request.GET.get('condition', '')
        device_type_filter = self.request.GET.get('device_type', '')

        if q:
            queryset = queryset.filter(
                Q(model__icontains=q) |
                Q(serial_number__icontains=q) |
                Q(device_type__name__icontains=q)
            )

        if condition_filter:
            queryset = queryset.filter(condition=condition_filter)

        if device_type_filter:
            queryset = queryset.filter(device_type_id=device_type_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['condition_choices'] = Device.Condition.choices
        context['device_type_choices'] = DeviceType.objects.all()
        context['selected_condition'] = self.request.GET.get('condition', '')
        context['selected_type'] = self.request.GET.get('device_type', '')
        return context


