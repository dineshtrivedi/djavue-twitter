from django.contrib.auth.models import User
from django.db.models import Q
from core.models import Following, Tweet


def follow(user, username):
    user_to_follow = User.objects.get(username=username)
    if Following.objects.filter(from_user=user, to_user=user_to_follow).count() == 0:
        Following.objects.create(from_user=user, to_user=user_to_follow)


def unfollow(user, username):
    user_to_unfollow = User.objects.get(username=username)
    Following.objects.filter(from_user=user, to_user=user_to_unfollow).delete()


def tweet(user, text):
    tweet = Tweet.objects.create(user=user, text=text)
    return tweet.to_dict_json()


def list_tweets(logged_user, username=None):
    if username:
        tweets = Tweet.objects.filter(user__username=username)
    else:
        if logged_user:
            query = Q(user__in=User.objects.filter(following_to__from_user=logged_user))
            query |= Q(user=logged_user)
            tweets = Tweet.objects.filter(query)
        else:
            tweets = Tweet.objects.all()

    tweets = tweets.order_by('-created_at')
    return [t.to_dict_json() for t in tweets]
