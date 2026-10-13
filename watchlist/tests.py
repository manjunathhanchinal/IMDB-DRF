from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from watchlist.models import StreamPlatform, WatchList, Review


class ReviewCreateAuthenticationTests(TestCase):
    def test_anonymous_user_cannot_create_review(self):
        response = APIClient().post(
            reverse('review-create', kwargs={'pk': 4}),
            data={},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ReviewCreateTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='reviewer', password='password')
        self.platform = StreamPlatform.objects.create(
            name='Test platform',
            about='Test platform',
            website='https://example.com',
        )
        self.movie = WatchList.objects.create(
            title='URL movie',
            storyline='A test movie',
            platform=self.platform,
        )
        self.other_movie = WatchList.objects.create(
            title='Other movie',
            storyline='Another test movie',
            platform=self.platform,
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_review_uses_movie_from_url_without_watchlist_in_request(self):
        response = self.client.post(
            reverse('review-create', kwargs={'pk': self.movie.pk}),
            data={'rating': 4, 'description': 'Good movie'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        review = Review.objects.get()
        self.assertEqual(review.watchlist, self.movie)
        self.assertEqual(response.data['watchlist'], self.movie.pk)

    def test_create_review_ignores_watchlist_from_request_body(self):
        response = self.client.post(
            reverse('review-create', kwargs={'pk': self.movie.pk}),
            data={
                'rating': 4,
                'description': 'Good movie',
                'watchlist': self.other_movie.pk,
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        review = Review.objects.get()
        self.assertEqual(review.watchlist, self.movie)
