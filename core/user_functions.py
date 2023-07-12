from .models import Profile, Post, LikePost, FollowersCount
from django.contrib.auth.models import User

def get_following(username: str) -> list:
    user_following = FollowersCount.objects.filter(follower=username)
    user_following_list = []
    for users in user_following:
        user_following_list.append(User.objects.get(username=users.user))
    return user_following_list