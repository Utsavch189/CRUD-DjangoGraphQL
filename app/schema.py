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
    """
    {
        allFiles{
          user,
          filename
        }
    }
    """
    aFiles=graphene.List(Filless,user=graphene.String())
    """
    {
        aFiles(user:"csvfgs"){
          user,
          filename
        }
    }
    """

    def resolve_allFiles(root,info):
        return Files.objects.all()
    
    def resolve_aFiles(root,info,user):
        return Files.objects.filter(user=user)

#CREATE..................
class Posts(graphene.Mutation):
    class Arguments:
        filename=graphene.String(required=True)
        user=graphene.String(required=True)

    creates=graphene.Field(Filless)

    @classmethod
    def mutate(cls,self,info,filename,user):
        post=Files(filename=filename,user=user)
        post.save()
        return Posts(creates=post)

"""
mutation abc{
  create(filename:"harry potter.jpg",user:"uts1"){
    creates{
      filename,
      user
    }
  }
"""

    
#UPDATE.........................
class Update(graphene.Mutation):
    class Arguments:
        filename=graphene.String(required=True)
        user=graphene.String(required=True)

    updates=graphene.Field(Filless)

    @classmethod
    def mutate(cls,self,info,filename,user):
        if(Files.objects.get(user=user)):        
            obj=Files.objects.get(user=user)
            obj.filename=filename
            obj.save()
            post=Files.objects.get(user=user)
            return Update(updates=post)
    
"""
mutation abc{
  update(filename:"harry pottersss.jpg",user:"uts1"){
    updates{
      filename,
      user
    }
  }
}
}
"""

#DELETE..............................
class Delete(graphene.Mutation):
    class Arguments:
        user=graphene.String(required=True)

    deletes = graphene.String()

    @classmethod
    def mutate(cls,self,info,user):
        if(Files.objects.get(user=user)):        
            obj=Files.objects.get(user=user)
            obj.delete()
            return Delete(deletes = "Post deleted Successfully")

"""
mutation abc{
  delete(user:"ygyg"){
   deletes
  }
}
"""

class Mutation(graphene.ObjectType):
    create = Posts.Field()
    update=Update.Field()
    delete=Delete.Field()

schema1 = graphene.Schema(query=Query)
schema2=graphene.Schema(query=Posts,mutation=Mutation)