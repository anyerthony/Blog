from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class blogViews(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'blog_list.html',context)