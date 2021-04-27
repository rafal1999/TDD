from django.urls import resolve 
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item
# Create your tests here.

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request=HttpRequest()
        response=home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Todo list</title>',html)
        self.assertTrue(html.endswith('</html>'))

    def test_home_page_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')     
        # self.assertEqual(response.status_code,302)
        # self.assertEqual(response['location'], '/')      
        #self.assertIn('A new list item',  response.content.decode()), "no nie działa"
        # self.assertTemplateUsed(response, 'hoe.html')
    
    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/')

    def test_displays_all_list_item(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')
        
        response = self.client.get('/')

        self.assertIn('item 1', response.content.decode())
        self.assertIn('item 2', response.content.decode())

class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_item=Item()
        first_item.text='The first list item'
        first_item.save()   

        second_item  = Item()  
        second_item.text = 'Item the second'
        second_item.save() 

        saved_items = Item.objects.all()    
        self.assertEqual(saved_items.count(), 2)

        first_saved_items = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_items.text, 'The first list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
