import graphene
from django.db import models
from graphene import Field, List, Int, ID, NonNull, ObjectType
from graphene_django import DjangoObjectType
from ..models import Filter
from .types import ImageFilterType


class ImageFiltersQuery(ObjectType):
    image_filters = NonNull(List(ImageFilterType))

    def resolve_image_filters(self, info):
        return Filter.objects.all()