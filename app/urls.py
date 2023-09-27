from django.urls import path
from graphene_django.views import GraphQLView
from app.schema import schema1,schema2
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("get", GraphQLView.as_view(graphiql=True,schema=schema1)),
    path("post", csrf_exempt(GraphQLView.as_view(graphiql=True,schema=schema2))),
]