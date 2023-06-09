"""OnlineShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ShopBasket.views import show_shop, show_basket, set_cookie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_shop, name = 'shop'),
    path('basket/', show_basket, name = 'basket'),
    path('set_cookie', set_cookie, name = 'set_cookie')
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)