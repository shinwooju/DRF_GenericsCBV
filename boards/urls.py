from django.urls import path

from .views import board_detail_delete_update, board_list_create, comment, comments_update_delete


app_name = 'boards'
urlpatterns = [
    path('', board_list_create),
    path('<int:pk>/', board_detail_delete_update),
    path('<int:pk>/comments/', comment),
    path('<int:pk>/comments/<int:comment_pk>', comments_update_delete)
]