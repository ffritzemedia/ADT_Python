#! /usr/bin/env python3
import unittest
from adt import Stack, wrongTypeException, getItemException

class TestStack(unittest.TestCase):

    def setUp(self):
        """Initialisierung vor jedem Test"""
        self.stack = Stack(None)  # Erstelle einen leeren Stack

    def test_push_and_top(self):
        """Testet das Hinzufügen von Elementen und das Abrufen des obersten Elements"""
        self.stack.push(10)
        self.assertEqual(self.stack.top(), 10)
        self.stack.push(20)
        self.assertEqual(self.stack.top(), 20)

    def test_pop(self):
        """Testet das Entfernen von Elementen"""
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)
        with self.assertRaises(getItemException):
            self.stack.pop()  # Sollte eine Ausnahme werfen, wenn der Stack leer ist

    def test_empty_stack(self):
        """Testet das Verhalten eines leeren Stacks"""
        with self.assertRaises(getItemException):
            self.stack.top()  # Sollte eine Ausnahme werfen, wenn der Stack leer ist
        with self.assertRaises(getItemException):
            self.stack.pop()  # Sollte eine Ausnahme werfen, wenn der Stack leer ist

    def test_push_wrong_type(self):
        """Testet das Hinzufügen eines Elements falschen Typs"""
        self.stack.push(10)
        with self.assertRaises(wrongTypeException):
            self.stack.push("string")  # Sollte eine Ausnahme werfen

if __name__ == '__main__':
    unittest.main()