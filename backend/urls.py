from django.urls import path
from . import views
from .views import NoteList, NoteDetail

urlpatterns = [
    path('<int:pk>/', NoteDetail.as_view(), name="detailcreate"),
    path('', NoteList.as_view(), name='listcreate'),
]