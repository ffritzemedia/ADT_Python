#! /usr/bin/env python3
import unittest
from adt import Queue, wrongTypeException, getItemException

class TestQueue(unittest.TestCase):

    def setUp(self):
        """Initialisierung vor jedem Test"""
        self.queue = Queue(None)  # Erstelle eine leere Warteschlange

    def test_enqueue_and_head(self):
        """Testet das Hinzufügen von Elementen und das Abrufen des vordersten Elements"""
        self.queue.enqueue(10)
        self.assertEqual(self.queue.head(), 10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.head(), 10)  # Das vorderste Element sollte unverändert bleiben

    def test_dequeue(self):
        """Testet das Entfernen von Elementen"""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.dequeue(), 10)  # Das erste Element sollte entfernt werden
        self.assertEqual(self.queue.dequeue(), 20)  # Das nächste Element sollte entfernt werden
        with self.assertRaises(getItemException):
            self.queue.dequeue()  # Sollte eine Ausnahme werfen, wenn die Warteschlange leer ist

    def test_empty_queue(self):
        """Testet das Verhalten einer leeren Warteschlange"""
        with self.assertRaises(getItemException):
            self.queue.head()  # Sollte eine Ausnahme werfen, wenn die Warteschlange leer ist
        with self.assertRaises(getItemException):
            self.queue.dequeue()  # Sollte eine Ausnahme werfen, wenn die Warteschlange leer ist

    def test_enqueue_wrong_type(self):
        """Testet das Hinzufügen eines Elements falschen Typs"""
        self.queue.enqueue(10)
        with self.assertRaises(wrongTypeException):
            self.queue.enqueue("string")  # Sollte eine Ausnahme werfen

if __name__ == '__main__':
    unittest.main()