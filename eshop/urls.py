from django.urls import path, include

from eshop.views import homepage_view, authorDetailView, CategoryDetailView, PaintDetailView, \
    AddToCartView, OrderDetailView, LoginView, LogoutView, RegistrationView, UpdateUserProfile

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

cart_urlpatterns = (
    [
        path('detail/<int:pk>/', OrderDetailView.as_view(), name='detail'),
        path('add/<int:pk>/', AddToCartView.as_view(), name='add'),
        # path('update/<int:pk>/', ActorUpdateView.as_view(), name='update'),
        # path('delete/<int:pk>/', ActorDeleteView.as_view(), name='delete'),
    ], 'cart'
)

auth_urlpatterns = (
    [
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('register/', RegistrationView.as_view(), name='register'),
        path('update/<int:pk>/', UpdateUserProfile.as_view, name='update'),
    ], 'auth'
)

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('author/', include(author_urlpatterns)),
    path('category/', include(category_urlpatterns)),
    path('paint/', include(paint_urlpatterns)),
    path('cart/', include(cart_urlpatterns)),
    path('auth/', include(auth_urlpatterns)),
]
