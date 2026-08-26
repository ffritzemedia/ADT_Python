"""Kompatibilitaetsimporte fuer die ADT-Klassen."""

from ADT.adt import (
    ADT,
    BinTree,
    DynArray,
    Queue,
    Stack,
    getItemException,
    wrongTypeException,
)

adt = ADT
bintree = BinTree
dynarray = DynArray
queue = Queue
stack = Stack

__all__ = [
    "ADT",
    "BinTree",
    "DynArray",
    "Queue",
    "Stack",
    "adt",
    "bintree",
    "dynarray",
    "getItemException",
    "queue",
    "stack",
    "wrongTypeException",
]