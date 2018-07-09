from django.db import models
from django.contrib.auth.models import User


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser")
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Following(models.Model):
    from_user = models.ForeignKey(User, related_name='followed_by')
    to_user = models.ForeignKey(User, related_name='following_to')

    class Meta:
        unique_together = ('from_user', 'to_user',)


class Tweet(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict_json(self):
        return {
            'id': self.id,
            'author_name': self.user.first_name,
            'author_username': self.user.username,
            'author_avatar': 'TODO',
            'created_at': self.created_at.isoformat(),
            'text': self.text,
        }