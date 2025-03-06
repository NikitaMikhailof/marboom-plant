from django.http import JsonResponse
from django.views import View
from .models import Equipment


class EquipmentAutocomplete(View):
    def get(self, request):
        query = request.GET.get('term', '')
        equipments = Equipment.objects.filter(title__icontains=query)[:10]
        results = [equipment.title for equipment in equipments]
        return JsonResponse(results, safe=False)