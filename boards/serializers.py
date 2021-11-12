from rest_framework import serializers
from .models        import Board, Comment


class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Board
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Comment
        fields = ['contents', 'board']

    # 아래의 function은 댓글을 추가할때 댓글내용과 게시글pk가 같이 표현되지 않게하기 위한 기능이다.
    # 원하는 필드를 return 해주는데 딕셔너리 형태로 작성하되 instance가 꼭 들어가야한다.
    def to_representation(self, instance):
        return {
            'contents': instance.contents,
        }

# 게시글을 불러올때 연결되어있는 댓글을 불러오기 위해서는 model은 Board이지만 댓글을 따로 지정해줘 fields에 추가해준다.
class BoardDetailSerializers(serializers.ModelSerializer):
    #댓글을 따로 지정해주고 여러개의 댓글이 가능하게 many = True를 넣어준다.
    comments = CommentSerializers(many = True)
    class Meta:
        model = Board
        fields = ['title','contents','comments']