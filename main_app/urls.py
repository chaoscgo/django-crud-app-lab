from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('members/', views.member_index, name='member-index'),
    path('members/<int:member_id>/', views.member_detail, name='member-detail'),
    path('members/create/', views.MemberCreate.as_view(), name='member-create'),
    path('members/<int:pk>/update/', views.MemberUpdate.as_view(), name='member-update'),
    path('members/<int:pk>/delete/', views.MemberDelete.as_view(), name='member-delete'),
    path(
        'members/<int:member_id>/add-game/', 
        views.add_game, 
        name='add-game'
    ),
    path('gears/create/', views.GearCreate.as_view(), name='gear-create'),
    path('gears/<int:pk>/', views.GearDetail.as_view(), name='gear-detail'),
    path('gears/', views.GearList.as_view(), name='gear-index'),
    path('gears/<int:pk>/update/', views.GearUpdate.as_view(), name='gear-update'),
    path('gears/<int:pk>/delete/', views.GearDelete.as_view(), name='gear-delete'),
    path('members/<int:member_id>/associate-gear/<int:gear_id>/', views.associate_gear, name='associate-gear'),
    path('members/<int:member_id>/remove-gear/<int:gear_id>/', views.remove_gear, name='remove-gear'),
    path('accounts/signup/', views.signup, name='signup'),
]
