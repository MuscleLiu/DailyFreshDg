from django.urls import path,re_path
from django.contrib.auth.decorators import login_required
from user.views import RegisterView,ActiveView,LoginView, UserInfoView, UserOrderView, AdderssView, LogoutView

app_name = 'apps.user'
urlpatterns = [
  # path('register',views.register, name='register'), # 注册
  path('register', RegisterView.as_view(),  name='register') ,# 注册
  re_path('active/(?P<token>.*)',ActiveView.as_view(), name='active'), # 用户激活
  path('login', LoginView.as_view(), name='login'), # 登录
  path('logout', LogoutView.as_view(), name='logout'), # 退出
  # path('', login_required(UserInfoView.as_view()), name='user'), # 用户中心信息页
  path('', UserInfoView.as_view(), name='user'), # 用户中心信息页
  re_path('order/(?P<page>\d+)', UserOrderView.as_view(), name='order'), # 用户中心订单页
  path('address', AdderssView.as_view(), name='address'), # 用户中心地址页

]
