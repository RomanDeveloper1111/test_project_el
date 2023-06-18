from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from back.models import Post
from django.contrib.auth.models import User
import os
from back.serializers import PostSerializer


class TestPosts(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(username='wqerq', password='qwer')
        self.user_2 = User.objects.create(username='wqffferq', password='qwfffer')

        self.post_1 = Post.objects.create(
                pk=1,
                image_s=str(os.path.basename('./images/small_correct_image.jpeg')),
                image_b=str(os.path.basename('./images/big_correct_image.jpeg')),
                author=self.user_1
             )

        self.post_2 = Post.objects.create(
            pk=2,
            image_s=str(os.path.basename('./images/small_correct_image.jpeg')),
            image_b=str(os.path.basename('./images/big_correct_image.jpeg')),
            author=self.user_2
        )

    def test_get_list(self):
        url = reverse('posts-list')
        response = self.client.get(url)
        serializer = PostSerializer([self.post_1, self.post_2], many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_detail(self):
        url = reverse('posts-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        serializer = PostSerializer(self.post_1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_my_posts(self):
        url = reverse('my_posts-list')
        self.client.force_authenticate(user=self.user_2)
        serializer = PostSerializer([self.post_2, ], many=True)
        response = self.client.get(url)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_my_posts(self):
        url = reverse('my_posts-detail', kwargs={'pk': 2})
        self.client.force_authenticate(user=self.user_2)
        serializer = PostSerializer(self.post_2)
        response = self.client.get(url)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)





