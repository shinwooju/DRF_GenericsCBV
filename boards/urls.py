from django.urls import path

from .views import BoardList, BoardDetail, CommentCreate, CommentUpdate


app_name = 'boards'

urlpatterns = [
    path('', BoardList().as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/comments/', CommentCreate.as_view()),
    path('<int:pk>/comments/<int:comment_pk>', CommentUpdate.as_view())
]