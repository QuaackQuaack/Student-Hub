from django.urls import path

from .views import HomePageView, DeletePageView, UpdatePageView, NotesDetailView, CreatePageView, PomodoroPageView

urlpatterns = [
        path("", HomePageView.as_view(), name = 'home'),
        path("<int:pk>/", NotesDetailView.as_view(), name = 'view'), 
        path("<int:pk>/delete/", DeletePageView.as_view(), name = 'delete'),
        path("<int:pk>/update/", UpdatePageView.as_view(), name = 'update'), 
        path("create/", CreatePageView.as_view(), name = 'create'),
        path("pomodoro/", PomodoroPageView.as_view(), name = 'pomodoro'), 

        ]

