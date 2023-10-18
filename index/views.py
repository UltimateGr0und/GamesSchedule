from django.http import HttpResponse
from index.models import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView, View
from index.utils import *
from index.forms import CreateEventForm
from django.contrib.auth.decorators import login_required
class Home(DataMixin, ListView):
    model = Event
    template_name = 'index/index.html'
    context_object_name = 'events'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='События')
        return dict(list(context.items()) + list(c_def.items()))

        # context['title'] = 'События'
        # context['cat_selected'] = 0
        # context['menu'] = menu
        # return context
    def get_queryset(self):
        return Event.objects.all()

class CategoryView(DataMixin, ListView):
    model = Event
    template_name = 'index/index.html'
    context_object_name = 'events'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['events'][0].category),
                                      cat_selected=context['events'][0].category.pk)
        return dict(list(context.items()) + list(c_def.items()))

        # context['title'] = 'События'
        # context['cat_selected'] = kwargs.get('cat_slug')
        # return context
    def get_queryset(self):
        cat = Category.objects.filter(slug=self.kwargs['cat_slug']).first()
        events = Event.objects.filter(category=cat)
        return events

class EventView(DataMixin, DetailView):
    model = Event
    template_name = 'index/event.html'
    slug_url_kwarg = 'event_slug'
    context_object_name = 'event'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['event'])
        return dict(list(context.items()) + list(c_def.items()))

class CreateEvent(DataMixin, CreateView):
    form_class = CreateEventForm
    template_name = 'index/addevent.html'
    raise_exception = True
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление события')
        return dict(list(context.items()) + list(c_def.items()))
@login_required(login_url="/admin")
def temp(request):
    return HttpResponse('temp')