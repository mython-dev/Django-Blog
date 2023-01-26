from django.shortcuts import render, get_object_or_404
from .models import Projects


from django.views.generic.list import ListView

# Create your views here.

def projects(request):
    projects = Projects.objects.all()
    date = Projects.objects.order_by('-date')

    context = {'projects': projects, "date": date}

    return render(request, './projects.html', context)


def detail_project(request, project_id):
    projects = get_object_or_404(Projects, pk=project_id)
    return render(request, './detail_project.html',{'projects':projects})



class Search(ListView):

    template_name = './projects.html'

    context_object_name = 'projects'

    paginate_by = 5

    def get_queryset(self):
        return Projects.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')

        return context

        
