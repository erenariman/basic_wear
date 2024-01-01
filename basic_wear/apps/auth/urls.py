from django.urls import path
from dj_rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)
from .views import (FacebookLogin, TwitterLogin, GitHubLogin, GoogleLogin, FacebookConnect,
                    TwitterConnect, GithubConnect)

urlpatterns = [
    path('facebook-login/', FacebookLogin.as_view(), name='fb_login'),
    path('twitter-login/', TwitterLogin.as_view(), name='twitter_login'),
    path('github-login/', GitHubLogin.as_view(), name='github_login'),
    path('google-login', GoogleLogin.as_view(), name='google_login'),
    path('facebook-connect/', FacebookConnect.as_view(), name='fb_connect'),
    path('twitter-connect/', TwitterConnect.as_view(), name='twitter_connect'),
    path('github-connect/', GithubConnect.as_view(), name='github_connect'),
    path(
        'socialaccounts/',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    path(
        'socialaccounts/<int:pk>/disconnect/',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    )
]
