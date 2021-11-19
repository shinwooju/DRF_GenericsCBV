from rest_framework import serializers
from .models        import Board, Comment


class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Board
        fields = '__all__'

# 편의를 위해 댓글의 id값을 불러오고 게시글의 pk값을 불러오는 'board'를 삭제합니다.
class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Comment
        fields = ['id','contents']

# 게시글을 불러올때 연결되어있는 댓글을 불러오기 위해서는 model은 Board이지만 댓글을 따로 지정해줘 fields에 추가해준다.
class BoardDetailSerializers(serializers.ModelSerializer):
    # 댓글을 따로 지정해주고 여러개의 댓글이 가능하게 many = True를 넣어준다.
    comments = CommentSerializers(many = True)
    class Meta:
        model = Board
        fields = ['title','contents','comments']