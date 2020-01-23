import graphene
from django.db.models import Q
from django.contrib.auth import get_user_model
from graphene import NonNull, ObjectType, List, Field, String, Union, ID, Int
from graphene_django import DjangoObjectType
from friendship.models import Friend, FriendshipRequest, Follow, Block

from address.graphql.types import AddressType
from social.models import Post
from social.graphql.types import PostType, FriendType, FriendshipRequestType, FollowType
from .types import UserType, ProfileType
from ..models import Profile


class UserAuth(ObjectType):
    me = Field(get_user_model())
    users = List(get_user_model())

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure!')
        return user

# Depricated use ProfileSearchQuery instead


class ProfileSearchQuery(ObjectType):
    profile_search = graphene.List(ProfileType, search=graphene.String(
    ), offset=Int(default_value=0), limit=Int(default_value=20))

    def resolve_profile_search(self, info, offset, limit, search=None, **kwargs):
        if search:
            return Profile.objects.filter(
                Q(username__icontains=search),
            ).exclude(Q(user__is_hidden=True)).distinct()[offset:offset+limit]

        return Profile.objects.all().exclude(Q(user__is_hidden=True)).distinct()[offset:offset+limit]


class GetAuthUserQuery(ObjectType):
    get_auth_user = Field(UserType)

    def resolve_get_auth_user(self, info):
        user = get_user_model().objects.get(id=info.context.user.id)
        if user.is_anonymous:
            raise Exception('You need to login')
        return user


class GetUserProfileQuery(ObjectType):
    get_user_profile = Field(ProfileType, username=String())

    def resolve_get_user_profile(self, info, username):
        profile = get_user_model().objects.get(username=username).profile
        return profile


class GetAuthUserProfileQuery(ObjectType):
    get_auth_user_profile = Field(ProfileType)

    def resolve_get_auth_user_profile(self, info):
        profile = info.context.user.profile
        return profile
