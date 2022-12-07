from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Team

class TeamListView(ListView):
    template_name = 'clubs/team_list_view.html'
    model = Team
    context_object_name = 'myteames'

class TeamDetailView(DetailView):
    template_name = 'clubs/team_detail_view.html'
    model = Team

class TeamCreateView(CreateView):
    template_name = 'clubs/team_create_view.html'
    model =Team
    context_object_name = 'myteames'
    fields = ["team_name","country_name", "team_color" ,"logo","author"]

class TeamUpdateView(UpdateView):
    template_name = 'clubs/team_update_view.html'
    model = Team
    fields = ["team_name","country_name", "team_color" ,"logo","author"]
    success_url = reverse_lazy('list_view')

class TeamDeleteView(DeleteView):
    template_name = 'clubs/team_delete_view.html'
    model = Team
    success_url = reverse_lazy('list_view')