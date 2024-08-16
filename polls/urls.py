from . import views
from django.urls import path
from . views import QuestionListView, QuestionCreateView

urlpatterns = [
    path("", QuestionListView.as_view(), name="index"),
    path("create/", QuestionCreateView.as_view(), name="create"),
]