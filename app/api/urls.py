from django.urls import path, include
from rest_framework import routers

from app.api.views import PostViewCountView, CreatorView, PostView, CommentView, CategoryView

router = routers.DefaultRouter()
router.register('creators', CreatorView)
router.register('posts', PostView)
router.register('comments', CommentView)
router.register('categories', CategoryView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/post-view-counts/<int:pk>/', PostViewCountView.as_view(), name='post-view-count'),
]
