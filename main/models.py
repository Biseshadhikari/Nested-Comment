from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null = False)
    body = models.TextField(null = False)
    Created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_response(self):
        return self.response.filter(parent = None)
    
    
class Response(models.Model):
    user = models.ForeignKey(User, null=False,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False,on_delete=models.CASCADE,related_name='response')
    parent = models.ForeignKey('self',null=True,blank = True,on_delete=models.CASCADE)
    body = models.TextField(null = False)
    Created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
    def get_response(self):
        return Response.objects.filter(parent = self)



