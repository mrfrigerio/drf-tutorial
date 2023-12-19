import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    if model_data:
        serializer = ProductSerializer(data=model_to_dict(model_data))
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
        return Response({"error": "not valid Json"})
