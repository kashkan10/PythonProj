from django.test import TestCase
from library.models import *

class AnimalTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="Tom", age="22")
        User.objects.create(name="Tim", age="21")
        Book.objects.create(name="Q", author="Mok",user=User.objects.get(name="Tom"))

    def test_of_age(self):
        tom = User.objects.get(name="Tom")
        tim = User.objects.get(name="Tim")
        self.assertEqual(tom.age, 22)
        self.assertEqual(tim.age, 21)

    def test_read_book(self):
        book = Book.objects.get(name="Q")
        tom = User.objects.get(name="Tom")
        tim = User.objects.get(name="Tim")
        self.assertEqual(book.user, tom)
        self.assertNotEqual(book.user, tim)

    def test_count_of_books_of_user(self):
        Book.objects.create(name="Q1", author="Moka", user=User.objects.get(name="Tom"))
        books = Book.objects.filter(user=User.objects.get(name="Tom"))
        books2= Book.objects.filter(user=User.objects.get(name="Tim"))
        self.assertEqual(books.count(), 2)
        self.assertEqual(books2.count(), 0)

    def test_change_of_book(self):
        Book.objects.create(name="Q1", author="Moka", user=User.objects.get(name="Tom"))
        book = Book.objects.get(name="Q1")
        book.name="Q2"
        self.assertEqual(book.name, "Q2")
        self.assertEqual(book.author, "Moka")