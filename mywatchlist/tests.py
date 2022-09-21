from django.test import TestCase, Client
from django.urls import resolve
from example_app.views import index
# Create your tests here.r

class WatchlistTest(TestCase):
    def test_html(self):
        response_html= Client().get('/mywatchlist/html/')
        self.assertEqual(response_html.status_code, 200)
    
    def test_xml(self):
        response_xml = Client().get('/mywatchlist/xml/')
        self.assertEqual(response_xml.status_code, 200)
        
    def test_json(self):
        response_json = Client().get('/mywatchlist/json/')
        self.assertEqual(response_json.status_code, 200)

