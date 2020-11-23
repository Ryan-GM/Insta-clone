from django.conf.urls import url
from django.conf.urls import url,include
from insta.views import PostLikeAPIToggle,PostLikeToggle
from . import views
from django.urls import path
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    url('', views.index, name='index'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('post/<id>', views.post_comment, name='comment'),
    path('post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    path('api/post/<id>/like', PostLikeAPIToggle.as_view(), name='liked-api'),
    url('like', views.like_post, name='like_post'),
    url('search/', views.search_profile, name='search'),
    url('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    url('follow/<to_follow>', views.follow, name='follow')
]