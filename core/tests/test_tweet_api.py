from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json

DESCARTE_TWEET_1 = 'I think thefore I exist'
NEWTON_FIRST_LAW_TWEET = 'First Law'
NEWTON_SECOND_LAW_TWEET = 'Second Law'


class TestTweetsApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.scientsts_users()

    def test_tweets_api(self):
        newton, eistein, descartes, annonymous = Client(), Client(), Client(), Client()
        newton.force_login(User.objects.get(username='@newton'))
        eistein.force_login(User.objects.get(username='@einstein'))
        descartes.force_login(User.objects.get(username='@descartes'))
        self._follow(newton, '@descartes')
        self._follow(eistein, '@descartes')
        self._follow(eistein, '@newton')
        self._follow(newton, '@einstein')
        self._unfollow(newton, '@einstein')
        self._tweet(descartes, DESCARTE_TWEET_1)
        self._tweet(newton, NEWTON_FIRST_LAW_TWEET)
        self._tweet(newton, NEWTON_SECOND_LAW_TWEET)
        self._tweet(eistein, 'E = MC2')
        self._tweet(eistein, 'Potato')
        self._assert_home_tweets(descartes, [])
        self._assert_home_tweets(newton, [DESCARTE_TWEET_1])
        self._assert_home_tweets(eistein, [NEWTON_SECOND_LAW_TWEET, NEWTON_FIRST_LAW_TWEET, DESCARTE_TWEET_1])
        self._assert_home_tweets(annonymous, ['Potato', 'E = MC2', NEWTON_SECOND_LAW_TWEET, NEWTON_FIRST_LAW_TWEET, DESCARTE_TWEET_1])
        self._assert_tweets_user(annonymous, '@einstein', ['Potato', 'E = MC2'])
        self._assert_tweets_user(newton, '@einstein', ['Potato', 'E = MC2'])

    def _follow(self, client, username):
        r = client.post('/api/follow', {'username': username})
        self.assertEqual(200, r.status_code)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)

    def _unfollow(self, client, username):
        r = client.post('/api/unfollow', {'username': username})
        self.assertEqual(200, r.status_code)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)

    def _tweet(self, client, text):
        r = client.post('/api/tweet', {'text': text})
        self.assertEqual(200, r.status_code)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)

    def _assert_home_tweets(self, client, expected_tweets_text):
        r = client.get('/api/list_tweets')
        self.assertEqual(200, r.status_code)
        tweets = json.loads(r.content.decode('utf-8'))
        current_tweets_text = [t['text'] for t in tweets]
        self.assertEquals(current_tweets_text, expected_tweets_text)

    def _assert_tweets_user(self, client, username, expected_tweets_text):
        r = client.get('/api/list_tweets', {'username': username})
        self.assertEqual(200, r.status_code)
        tweets = json.loads(r.content.decode('utf-8'))
        current_tweets_text = [t['text'] for t in tweets]
        self.assertEquals(current_tweets_text, expected_tweets_text)