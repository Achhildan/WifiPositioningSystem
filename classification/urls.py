from django.urls import path
from . import views



urlpatterns = [
    path('', views.FittingModel.as_view(), name="post_home"),
    path('lokasi/', views.GetLokasi.as_view(), name="lokasi_semua"),
    path('predict/', views.PredictModel.as_view(), name="post_detail")
]
