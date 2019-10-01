from django.db import models
from django.contrib.auth.models import User
import graphene
from graphene import NonNull, ObjectType, List, Field, String, Union, ID
from graphene_django import DjangoObjectType
from address.models import Address, Country
from .models import Profile


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        only_fields = {
            "iso_code",
            "name"
        }


class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        only_fields = {
            "address_line1",
            "address_line2",
            "postal_code",
            "city",
            "state_province",
            "country"
        }


class ProfileType(DjangoObjectType):
    user_name = String()
    full_name = String()
    address = Field(AddressType)

    class Meta:
        model = Profile
        only_fields = {
            "id",
            "user",
            "profile_avatar",
            "bio",
            "location",
            "birth_date",
            "interests",
        }

    def resolve_user_name(self, info):
        return self.user.username

    def resolve_full_name(self, info):
        return self.user.full_name

    def resolve_address(self, info):
        return self.user.address


class UserType(DjangoObjectType):
    address = Field(AddressType)
    profile = Field(ProfileType)

    class Meta:
        model = User
        only_fields = {
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
        }


class UserListQuery(ObjectType):
    users = NonNull(List(ProfileType))

    def resolve_users(self, info):
        return Profile.objects.all()


class UserQuery(ObjectType):
    user = Field(UserType, user_id=ID())

    def resolve_user(self, info, user_id):
        return User.objects.get(id=user_id)


class UserAuth(ObjectType):
    me = Field(User)
    users = List(User)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure!')
        return user
