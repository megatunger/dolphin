from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic

class ElementList(generic.TemplateView):
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'element/index.html'
