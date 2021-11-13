from django.urls import path

from .views import BoardDetailAPIView, BoardListAPIView, CommentCreateAPIView, CommentUpdateDeleteAPIView


app_name = 'boards'

urlpatterns = [
    path('', BoardListAPIView.as_view()),
    path('<int:pk>/', BoardDetailAPIView.as_view()),
    path('<int:pk>/comments/', CommentCreateAPIView.as_view()),
    path('<int:pk>/comments/<int:comment_pk>', CommentUpdateDeleteAPIView.as_view())
]