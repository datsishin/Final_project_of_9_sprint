from django.urls import pathfrom rest_framework.routers import DefaultRouterfrom .views import UserViewSet, PostViewSet, CommentViewSetrouter = DefaultRouter()router.register('api/v1/users', UserViewSet)# router.register('api/v1/posts/<int:pk>/comment', CommentViewSet)router.register('api/v1/posts', PostViewSet)# , {'put': 'put', 'patch': 'retrieve'}# , {'get': 'list', 'put': 'put', 'patch': 'retrieve'}# (actions={#         'get': 'list',#         'post': 'create',#         'put': 'update',#         'patch': 'retrieve',#     }))