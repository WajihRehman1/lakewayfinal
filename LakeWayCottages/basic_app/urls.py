
from django.urls import path
from basic_app import views
app_name='basic_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('createFeature/',views.createFeature.as_view(),name='createFeature'),
    path('updateFeature/<int:pk>/',views.updateFeature.as_view(),name='updateFeature'),
    path('deleteFeature/<int:pk>/', views.deleteFeature.as_view(), name='deleteFeature'),
    path('createApartment/',views.createApartment.as_view(),name='createApartment'),
    path('updateApartment/<int:pk>/',views.updateApartment.as_view(),name='updateApartment'),
    path('deleteApartment/<int:pk>/', views.deleteApartment.as_view(), name='deleteApartment'),
    path('email/',views.contactMail,name='mail'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.user_logout,name='logout')
]

