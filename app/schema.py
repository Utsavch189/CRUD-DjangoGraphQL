import graphene
from .models import Files
from graphene_django import DjangoObjectType

class Filless(DjangoObjectType):
    class Meta:
        model=Files
        fields=("filename","user")

#GET...................
class Query(graphene.ObjectType):

    allFiles=graphene.List(Filless)
    aFiles=graphene.List(Filless,user=graphene.String())

    def resolve_allFiles(root,info):
        return Files.objects.all()
    
    def resolve_aFiles(root,info,user):
        return Files.objects.filter(user=user)

#CREATE..................
class Posts(graphene.Mutation):
    class Arguments:
        filename=graphene.String(required=True)
        user=graphene.String(required=True)

    post=graphene.Field(Filless)

    @classmethod
    def mutate(cls,self,info,filename,user):
        post=Files(filename=filename,user=user)
        post.save()
        return Posts(post=post)


    
#UPDATE.........................
class Update(graphene.Mutation):
    class Arguments:
        filename=graphene.String(required=True)
        user=graphene.String(required=True)

    post=graphene.Field(Filless)

    @classmethod
    def mutate(cls,self,info,filename,user):
        if(Files.objects.get(user=user)):        
            obj=Files.objects.get(user=user)
            obj.filename=filename
            obj.save()
            post=Files.objects.get(user=user)
            return Posts(post=post)
    
#DELETE..............................
class Delete(graphene.Mutation):
    class Arguments:
        user=graphene.String(required=True)

    msg = graphene.String()

    @classmethod
    def mutate(cls,self,info,user):
        if(Files.objects.get(user=user)):        
            obj=Files.objects.get(user=user)
            obj.delete()
            return Delete(msg = "Post deleted Successfully")


class Mutation(graphene.ObjectType):
    create = Posts.Field()
    update=Update.Field()
    delete=Delete.Field()

schema1 = graphene.Schema(query=Query)
schema2=graphene.Schema(query=Posts,mutation=Mutation)