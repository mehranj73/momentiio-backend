from django.db import models
import graphene
from graphene import Field, Int, List, String
from graphene_django import DjangoObjectType
from friendship.models import Friend, FriendshipRequest, Follow, Block

from ..models import Post, Comment, Like


class LikeType(DjangoObjectType):
    class Meta:
        model = Like


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        only_fields = [
            "id",
            "user",
            "photo",
            "comment",
            "date_created"
        ]


class PostType(DjangoObjectType):
    comment_count = Int()
    like_count = Int()
    recent_comments = List(CommentType)

    class Meta:
        model = Post
        only_fields = [
            "id",
            "user",
            "caption",
            "photo",
            "date_created",
            "date_updated"
        ]

    def resolve_comment_count(self, info):
        return self.comments.all().count()

    def resolve_like_count(self, info):
        return self.likes.all().count()

    def resolve_recent_comments(self, info):
        return self.comments.all().order_by('-date_created')[:3]


class FriendType(DjangoObjectType):
    class Meta:
        model = Friend


class FriendshipRequestType(DjangoObjectType):
    class Meta:
        model = FriendshipRequest


class FollowType(DjangoObjectType):
    class Meta:
        model = Follow
