from django.urls import path
from .views import TeamListView, TeamDetailView, TeamCreateView,TeamUpdateView,TeamDeleteView

urlpatterns = [
    path('', TeamListView.as_view(), name='list_view'),
    path('<int:pk>', TeamDetailView.as_view(), name='detail_view'),
    path('create', TeamCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', TeamUpdateView.as_view(), name='update_view'),
    path('delete/<int:pk>', TeamDeleteView.as_view(), name='delete_view'),
    ]