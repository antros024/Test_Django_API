from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from .models import Articlesdata

class ArticlesdataTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.article = Articlesdata.objects.create(title='Django', content='Django is a high-level Python web framework', author='admin')

    def test_list(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        response = self.client.post('/articles/', {'title': 'Articles', 'content': 'Watatagain', 'author': 'Chose'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create(self):
        response = self.client.post('/articles/', {'title': '', 'content': '', 'author': ''})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve(self):
        response = self.client.get(f'/articles/{self.article.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_retrieve(self):
        response = self.client.get(f'/articles/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update(self):
        response = self.client.put(f'/articles/{self.article.id}/', {'title': 'Articles40', 'content': 'Watatagain', 'author': 'Chose'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_invalid_update(self):
        response = self.client.put(f'/articles/{self.article.id}/', {'title': '', 'content': '', 'author': ''})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_update(self):
        response = self.client.put(f'/articles/100/', {'title': 'Articles', 'content': 'Watatagain', 'author': 'Chose'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete(self):
        response = self.client.delete(f'/articles/{self.article.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = self.client.delete(f'/articles/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)