from django.test import TestCase, Client
from .models import Item

class MainTest(TestCase):
    def setUp(self):
        """
        membuat instance klien yang dapat digunakan untuk melakukan permintaan HTTP.
        """
        self.client = Client()

    def test_main_url_exists(self):
        """
        Menguji apakah URL utama ('/main/') ada dan mengembalikan kode status 200 (OK) saat diakses.
        """
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_uses_main_template(self):
        """
        Menguji apakah tampilan 'main' menggunakan template 'main.html'.
        """
        response = self.client.get('/main/')
        self.assertTemplateUsed(response, 'main.html')
        
    def test_create_item_model(self):
        """
        Menguji pembuatan instance model Item dan memeriksa atribut-atributnya, 
        seperti nama, jumlah, deskripsi, kode, dan harga.
        """
        item = Item.objects.create(
            name='Test Name',
            amount=0,
            description='Test Description',
            price=0
        )
        # Testing
        self.assertEqual(item.name, 'Test Name')
        self.assertEqual(item.amount, 0)
        self.assertEqual(item.description, 'Test Description')
        self.assertEqual(item.price, 0)
