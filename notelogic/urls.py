from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .import views
from . views import MyTokenObtainPairView

urlpatterns = [
    path('notes/', views.getNotes, name="notes"),
    path('notes/<int:pk>/', views.getNote, name="note"),
    path('notes/<int:pk>/update/', views.updateNote, name="update-note"),
    path('notes/<int:pk>/delete/', views.deleteNote, name="delete-blog"),
    path('notes/notes/', views.getMyNotes, name="mynotes"),
    path('notes/create/', views.createNote, name="create-note"),
    path('notes/<int:pk>/comments/', views.getComments, name="comments"),

    # Like Comments
    path('comments/create/', views.createComment, name="create-comment"),
    path('comments/<int:pk>/delete/', views.deleteComment, name="delete-comment"),
    path('notes/<int:pk>/addlike/', views.addLike, name="add-like"),
    path('notes/<int:pk>/removelike/', views.removeLike, name="remove-like"),

    # User
    path('register/', views.registerUser, name="register"),
    path('profile/<int:pk>/', views.getProfile, name="getProfile"),

    # Authentication
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Blog Categories
    path('notes/category/', views.getCategory, name="category"),

]


