from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Movies
# Create your tests here.

class MoviesTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username="tester",password="tester")
        self.Movie = Movies.objects.create(title="tester", user=self.user, description="test")

    def test_home_page_status(self):
        url = reverse('movies_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_page_response(self):
        url = reverse('movies_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'movies/movie-list.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_home_page_context(self):
        url = reverse('movies_list')
        response = self.client.get(url)
        movies_list = response.context['movie']
        self.assertEqual(len(movies_list), 1)
        self.assertEqual(movies_list[0].title, "tester")
        self.assertEqual(movies_list[0].description,"test")
        self.assertEqual(movies_list[0].user.username, "tester")

    def test_detail_page_status_code(self):
        url = reverse('movies_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('movies_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'movies/movie-details.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_detail_page_context(self):
        url = reverse('movies_detail',args=(1,))
        response = self.client.get(url)
        movies_list = response.context['movies']
        self.assertEqual(movies_list.title, "tester")
        self.assertEqual(movies_list.description,"test")
        self.assertEqual(movies_list.user.username, "tester")

    
    def test_create_view(self):
        obj={
            'title':"test2",
            'user':self.user.id,
            'description': "info..."
            
        }

        url = reverse('movies_create')
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertEqual(len(Movies.objects.all()),2)

    def test_update_view(self):
        obj={
            'title':"test2",
            'user':self.user.id,
            'description': "info..."
            
        }

        url = reverse('movies_update', args=(1,))
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertRedirects(response, reverse('movies_list'))

    
    def test_delete_view(self):
        url = reverse('movies_delete', args=(1,))
        response = self.client.post(path=url,follow=True)
        self.assertRedirects(response, reverse('movies_list'))


    def test_str_method(self):
        self.assertEqual(str(self.Movie),"tester")


    def test_create_response(self):
        url = reverse('movies_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'movies/movie-create.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_update_response(self):
        url = reverse('movies_update', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response,'movies/movie-update.html')
        self.assertTemplateUsed(response, '_base.html')


    def test_delete_response(self):
        url = reverse('movies_delete', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response,'movies/movie-delete.html')
        self.assertTemplateUsed(response, '_base.html')