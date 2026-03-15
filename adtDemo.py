#! /usr/bin/env python3
from adt import *

#Tests für den Datentypen Stack
stack = Stack(0) #Ein neuer Stack mit dem Item 0 wird angelegt, dadurch wird der Datentyp int für den Inhalt des Stapels festgelegt

#Das Hinzufügen einers anderen Datentypen als den initialisierten Datentypen löst einen Fehler aus
try:
    stack.push("String") 
except TypeError as err:
    print(err)

for i in range(1,4):
    stack.push(i) #Daten vom Typ int werden auf den Stapel gelegt.

print(stack)

while not stack.isEmpty(): #Die Schleife läuft, bis der Stapel leer ist.
    print('Inhalt: ',stack.pop(),', Länge: ', len(stack)) #Inhalt und Länge des Stacks werden asugegeben.

stack.push("String") #Ein leerer Stapel kann mit einem anderen Datentypen neu initialisiert werden.
print(stack.pop())

#Tests für den Datentypen Queue
queue = Queue(0) #Eine neue (Warte)Schlange wird mit dem Inhgalt 0 angelegt, dadurch wird der Datentyp für den Inhalt der Schlange festgelegt

#Das Hinzufügen eines anderen Datentypen als den für die Schlange initialisierten Datentypen löst einen Fehler aus.
try:
    queue.enqueue('String')
except TypeError as err:
    print(err)

for i in range(1,4):
    queue.enqueue(i) #Daten vom Typ int werden am Ende der Schlange hinzugefügt

print(queue)

for _ in range(len(queue)):
    print('Inhalt: ', queue.dequeue(), ', Länge: ', len(queue)) #Inhalt und Länge der Schlange werden ausgegeben.

queue.enqueue('String') #Eine leere Schlange kann für einen neuen Datentypen neu initialisiert werden.
print(queue.dequeue())

#Tests für den Datentypen DynArray
dynArray = DynArray(0) #Ein neues dynamsiches Array wird mit dem Inhalt 0 angelegt, damit ist der Inhaltstyp int festgelegt

dynArray.append(3) #Ein neues Element mit dem Inhalt 3 wird am Ende der dynamischen Reihung angehängt.
#Das Anhängen eines anderen Datentypen als int erzeugt einen Fehler
try:
    dynArray.append('String')
except TypeError as err:
    print(err)

#Das Andern des Inhaltes mit einem anderen Datentypen als int erzeugt einen Fehler
try:
    dynArray.setItem('String') #Wird kein Index angegeben, wird automatisch am Anfang des dynamischen Arrays hinzugefügt
except TypeError as err:
    print(err)

dynArray.insertAt(2,1) #Ein neues Element mit dem Inhalt 2 wird an der Stelle 1 (2. Element der dynamischen Reihung) eingefügt.
dynArray.setItem(10,1) #Der Inhalt des Elementes an der zweiten Stelle wird auf 10 gesetzt.
dynArray.delete(2) #Das Element an der Stelle 2 (3. Element der dynamischen Reichung) wird entfernt (hierbei handelt es sich um die letzte Stelle).
dynArray.insertAt(1, dynArray.getLength()) #Ein neues Element mit dem Inhalt 1 wird an die dynamische Reihung angehängt.
dynArray.delete(1) #Ein inneres Element wird aus der dynamischen Reihung entfernt.

print(dynArray)
while not dynArray.isEmpty():
    print(dynArray.delete()) #delete() gibt den Inhalt des ersten Elementes aus und löscht das erste Element. In die Klammer kann eine beliebige Stelle des Arrays eingesetzt werden.

dynArray.setItem('String') #Bei einer leeren dynamischen Reihung kann der Datentyp neu festgelegt werden.
print(dynArray.getItem())

#Demonstration des Datentypen BinTree
tree = BinTree() #erzeugt einen leeren Binärbaum
print('Ist der Baum leer? ', tree.isEmpty())
tree.setItem('Wurzel') #Belegt den Wurzelknoten mit dem Inhalt 'Wurzel' und legt den Datentypen für den Binärbaum fest
print('Der Baum hat den Inhalt "', tree.getItem(), '" und den Typ: ', tree.itemType, sep = "")
tree.setLeft(BinTree('linkes Kind')) #Üergibt einen Baum mit Inhalt 'linkes Kind' als linken Teilbaum
tree.setRight((BinTree('rechtes Kind')))
print(len(tree)) #Gibt die Anzahl der Elemente aus.
tree.getLeft().setRight(BinTree('r Enkel vom l Kind')) #Fügt einen 'Enkelknoten' hinzu
print('Ist das "linke Kind" ein Blatt? ', tree.getLeft().isLeaf())
print('Ist der "Enkelknoten" ein Blattknoten? ', tree.getLeft().getRight().isLeaf())
print(tree.preorder())
print(tree.inorder())
print(tree.postorder())
print(tree.levelorder())
tree.deleteRight()
print(tree.levelorder())
try:
    tree.setRight('Kein Baum erzeugt einen Fehler')
except TypeError as err:
    print(err)
try:
    tree.setRight(BinTree(5)) #Falscher Datentyp erzeugt einen Fehler
except TypeError as err:
    print(err)
try:
    tree.setItem(5) #Falscher Datentyp erzeugt einen Fehler
except TypeError as err:
    print(err)
    