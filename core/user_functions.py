from .models import Profile, Post, LikePost, FollowersCount, HashTag
from django.contrib.auth.models import User
from random import choice
from .general_functions import fetch_images

def get_following(username: str) -> list:
    user_following = FollowersCount.objects.filter(follower=username)
    user_following_list = []
    for users in user_following:
        user_following_list.append(User.objects.get(username=users.user))
    return user_following_list

def get_hash_feed(username: str, count: int = 5) -> list:
    hashtags = list(HashTag.objects.filter(user=username))
    feed = []
    req_list = []
    for cnt in range(count):
        hashtag = choice(hashtags)
        req_list.append((hashtag.hashtag,hashtag.page_id))
        hashtag.page_id += 1
        hashtag.save()
    for image in fetch_images(req_list):
        post = Post(user=image["hashtag"], url=image["url"], caption=image["desc"])
        feed.append(post)

    return feed