from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('CheckInternet',views.CheckInternet,name='CheckInternet'),
    path('CheckInternet',views.CheckInternet,name='CheckInternet'),
    path('MacIp',views.MacIp,name='MacIp'),
    path('NetSpeed',views.NetSpeed,name='NetSpeed'),
    path('Iploc',views.IpLoc,name='IpLoc'),
    path('Pinloc',views.PinLoc,name='PinLoc'),
    path('Utube',views.Utube,name='Utube'),
    path('UtubeDesc',views.UtubeDesc,name='UtubeDesc'),
    path('downloadcv',views.downloadcv,name='downloadcv'),

    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
