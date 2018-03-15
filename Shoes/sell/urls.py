from django.urls import path
from  .views import HomeView, ShoeListView, ShoeCreateView, ShoeList,ShoeDetail, WelcomeTemplateView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'sell'
urlpatterns = [
    path('', ShoeListView.as_view(), name='home'),
    path('create/', ShoeCreateView.as_view(), name='create'),
    path('welcome/', WelcomeTemplateView.as_view(), name='welcome'),
    path('shoes/', ShoeList.as_view(), name='shoe_list'),
    path('shoes/<int:pk>/', ShoeDetail.as_view(), name='detail'),


]

urlpatterns = format_suffix_patterns(urlpatterns)

