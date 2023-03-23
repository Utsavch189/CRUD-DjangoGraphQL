from django.urls import path
from graphene_django.views import GraphQLView
from app.schema import schema1,schema2

urlpatterns = [
    path("get", GraphQLView.as_view(graphiql=True,schema=schema1)),
    path("post", GraphQLView.as_view(graphiql=True,schema=schema2)),
]