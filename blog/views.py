from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic.list import ListView


# Create your views here.

def blog(request):

    blogs = Blog.objects.all()

    blogs = Blog.objects.order_by('-date')

    return render(request, './blog.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, './detail.html',{'blog':blog})


class Search(ListView):

    template_name = './blog.html'

    context_object_name = 'blogs'

    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')

        return context