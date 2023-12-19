from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductListCreateAPIView.as_view()),
    # path("", views.product_alt_view),
    # path("", views.ProductMixinView.as_view()),
    path("<int:pk>/", views.ProductRetrieveUpdateDestroyAPIView.as_view()),
    # path("<int:pk>/update/", views.ProductRetrieveUpdateDestroyAPIView.as_view()),
]
