from core.models import User, Tweet, Following


def get_details(logged_user, username):
    user = User.objects.get(username=username)
    q = Tweet.objects.filter(user=user).order_by('-created_at')
    last_tweet_text = ''
    if q.count() > 0:
        last_tweet_text = q[0].text

    iFollow = False
    if logged_user:
        iFollow = Following.objects.filter(from_user=logged_user, to_user=user).count() > 0

    return {
        'username': user.username,
        'avatar': "TODO",
        'last_tweet': last_tweet_text,
        'iFollow': iFollow
    }