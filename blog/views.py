from django.shortcuts import render
from blog.models import BlogPost
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, Context
# Create your views here.


def archive(request):
    t = loader.get_template('archive.html')
    posts = BlogPost.objects.all()
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))
