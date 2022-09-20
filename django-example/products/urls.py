from django.urls import path

from products.views import ProductViewSet, UserAPIView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get' : 'list',
        'post' : 'create'
    })),
    path('products/<int:id>', ProductViewSet.as_view({
        'get' : 'retrieve',
        'put' : 'update',
        'delete' : 'remove'
    })),
    path('user', UserAPIView.as_view())
]