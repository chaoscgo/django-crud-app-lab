from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('members/', views.member_index, name='member-index'),
    path('members/<int:member_id>/', views.member_detail, name='member-detail'),
    path('members/create/', views.MemberCreate.as_view(), name='member-create'),
    path('members/<int:pk>/update/', views.MemberUpdate.as_view(), name='member-update'),
    path('members/<int:pk>/delete/', views.MemberDelete.as_view(), name='member-delete'),
]
