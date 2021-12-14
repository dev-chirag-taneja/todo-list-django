from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete

urlpatterns = [
    path("", TodoList.as_view(), name="todos"),
    path("todo/<int:pk>/", TodoDetail.as_view(), name="todo"),
    path("create-todo/", TodoCreate.as_view(), name="create-todo"),
    path("update-todo/<int:pk>", TodoUpdate.as_view(), name="update-todo"),
    path("delete-todo/<int:pk>", TodoDelete.as_view(), name="delete-todo"),
]

