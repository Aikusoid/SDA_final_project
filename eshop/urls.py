from django.urls import path, include

from eshop.views import homepage_view, authorDetailView, CategoryDetailView, PaintDetailView

author_urlpatterns = (
    [
        path('detail/<int:pk>/', authorDetailView, name='detail'),
        # path('create/', ActorCreateView.as_view(), name='create'),
        # path('update/<int:pk>/', ActorUpdateView.as_view(), name='update'),
        # path('delete/<int:pk>/', ActorDeleteView.as_view(), name='delete'),
    ], 'author'
)

category_urlpatterns = (
    [
        path('detail/<int:pk>/', CategoryDetailView.as_view(), name='detail'),
        # path('create/', ActorCreateView.as_view(), name='create'),
        # path('update/<int:pk>/', ActorUpdateView.as_view(), name='update'),
        # path('delete/<int:pk>/', ActorDeleteView.as_view(), name='delete'),
    ], 'category'
)

paint_urlpatterns = (
    [
        path('detail/<int:pk>/', PaintDetailView.as_view(), name='detail'),
        # path('create/', ActorCreateView.as_view(), name='create'),
        # path('update/<int:pk>/', ActorUpdateView.as_view(), name='update'),
        # path('delete/<int:pk>/', ActorDeleteView.as_view(), name='delete'),
    ], 'paint'
)

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('author/', include(author_urlpatterns)),
    path('category/', include(category_urlpatterns)),
    path('paint/', include(paint_urlpatterns)),
]
