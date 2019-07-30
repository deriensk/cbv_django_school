from django.urls import path, include
from cbv_app import views

app_name = 'cbv_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
]
# ?P<pk>[-\w]+ used in django 1.11 and above instead of <int:pk>