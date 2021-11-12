from .models      import Board, Comment
from .serializers import BoardSerializers, CommentSerializers, BoardDetailSerializers

from rest_framework.decorators import api_view
from rest_framework.response   import Response
from rest_framework            import status


# 게시글의 목록과 생성
@api_view(['POST','GET'])
def board_list_create(request):
# 게시글 목록 불러오기
    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardSerializers(boards, many = True) # Many = True 해줘야 여러 객체들을 불러올 수 있습니다.
        return Response(serializer.data, status = status.HTTP_200_OK)

# 게시글 생성하기
    elif request.method == 'POST':
        serializer = BoardSerializers(data = request.data)
        if serializer.is_valid(): # 유효성 검사 True/False값으로 결과값을 지정해줄 수 있다.
            serializer.save() # 저장
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

# 게시글불러오기와 수정, 삭제
@api_view(['GET','DELETE','PUT'])
def board_detail_delete_update(request, pk):
# 게시글 불러오기
    if request.method == 'GET':
        # 사용자가 요청한 path Parameter에 넣은 게시글의 pk값 불러오는 게시글의 pk와 일치하는지 검증
        board = Board.objects.get(pk = pk) 
        if board == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = BoardDetailSerializers(board)  # 여기선 하나를 가져오기 때문에 Many(x)
        return Response(serializer.data, status = status.HTTP_200_OK)

# 게시글 삭제하기
    elif request.method == 'DELETE':
        board = Board.objects.get(pk = pk)
        if board == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        board.delete()
        return Response(status = status.HTTP_200_OK)

# 게시글 수정하기
    elif reqeust.method == 'PUT':
        board = Board.objects.get(pk = pk)
        if board == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        # 수정하기위한 보드 데이터를 불러와 client 요청에 따른 data를 담아주기, 부분적인 수정을 위해 patial = True를 해주어야함
        serializer = BoardSerializers(board, data = request.data, patial = True) 
        if serializer.is_valid(): # 수정 또한 유효성 검사가 필요
            serializer.save()
            return Response(serializer.date, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

# 게시글에 댓글달기
@api_view(['POST'])
def comment(request, pk):
# 게시글 댓글추가
    if request.method == 'POST':
        board = Board.objects.get(pk = pk) # 클라이언트가 요청하는 게시글
        if board == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        # ForeignKey로 연결되있는 게시글의 아이디를 같이 요청해야지 client가 요청한 게시글에 댓글을 추가하기위한 로직
        request.data['board'] = board.id 
        serializer = CommentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)

# 댓글 수정,삭제
@api_view(['PUT','DELETE'])
#여기서 pk는 게시글의 pk, urls.py에서 필요로 하기에 view에서 사용은 안하지만 선언은 해준다.
def comments_update_delete(request, pk, comment_pk):
#게시글 댓글 삭제
    if request.method == 'DELETE':
        #내가 수정하고자 요청한 댓글의 pk와 get으로 가져오는 pk
        comment = Comment.objects.get(pk = comment_pk) 
        if comment == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        comment.delete()
        return Response(status = status.HTTP_200_OK)

#게시글 댓글 수정
    elif request.method == 'PUT':
        comment = Comment.objects.get(pk = comment_pk)
        if comment == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        #게시글 수정과 같은방법으로 진행해준다.
        serializer = CommentSerializers(comment, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)