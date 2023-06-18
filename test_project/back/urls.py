from rest_framework.routers import SimpleRouter
from back.views import PostViewSet, MyPostsViewSet
from django.urls import include, path

router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'my_posts', MyPostsViewSet, basename='my_posts')

urlpatterns = [
    path(r'', include(router.urls)),
]
