from .models      import Board, Comment
from .serializers import BoardSerializers, CommentSerializers, BoardDetailSerializers

from rest_framework          import generics, status
from rest_framework.response import Response


# 게시글의 목록과 생성
class BoardList(generics.ListCreateAPIView):
    queryset         = Board.objects.all()
    serializer_class = BoardSerializers

# 게시글불러오기와 수정, 삭제
class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializers

    '''1개의 게시글을 불러올 때 댓글을 같이 불러와야 한다.
    'GET'요청이 들어올 때 불러오는 serializer_class에 따로 생성한
    Serializers를 불러오게 합니다.'''
    def get_serializer_class(self):
        if self.request.method == 'GET':
            self.serializer_class = BoardDetailSerializers
        return self.serializer_class

# 게시글에 댓글달기
class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    #board = pk값을 지정해서 원하는 게시글의 댓글만 생성하게끔 오버라이드한다.
    def create(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, pk)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #save()변수를 지정해 시리얼라이저에서 따로 지정해줄 필요 없다.
    def perform_create(self, serializer, pk):
        serializer.save(board_id = pk)

# 댓글 수정,삭제
class CommentUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    lookup_url_kwarg = 'comment_pk'