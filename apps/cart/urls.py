from django.urls import path
from apps.cart.views import CarDeleteView, CartAddView, CartInfoView,CartUpdateView
app_name = 'apps.cart'
urlpatterns = [
    path('', CartInfoView.as_view(), name='cart'), # 购物车页面
    path('add', CartAddView.as_view(), name='add'), # 显示购物车页
    path('update', CartUpdateView.as_view(), name='update'), # 显示购物车页
    path('delete', CarDeleteView.as_view(), name='delete'), # 显示购物车页
]
