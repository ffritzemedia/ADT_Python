#own exceptions
class getItemException(Exception):
    pass

#ADT Oberklasse
class ADT():
    def __init__(self, item = None):
        self.__item = item
        self.__next = None
    
    @property
    def item(self):
        return self.__item
    @item.setter
    def item(self, item):
        if self.__item is None or isinstance(item, type(self.__item)):
            self.__item = item
        else:
            raise TypeError('Type of item is ', type(item), ', but must be ', type(self.__item))
    
    def isEmpty(self):
        """Wenn kein Element enthalten ist wird der Wert 'True' zurückgegeben, ansonsten 'False'"""
        return self.__item is None and self.__next is None
    
    def __len__(self):
        """Die Anzahl der Elemente wird zurückgegeben"""
        if self.isEmpty():
            return 0
        elif self.__next is None:
            return 1
        else:
            return 1 + self.__next.__len__()
    
    def __str__(self):
        """Gibt eine lesbare Darstellung des ADT zurück."""
        elements = []
        current = self
        while current is not None:
            elements.append(str(current.item))
            current = current.__next
        return "[" + ", ".join(elements) + "]"

    def __repr__(self):
        """Gibt eine detaillierte Darstellung des ADT zurück, die nützlich für Debugging ist."""
        return f"ADT(item={self.__item!r}, next={repr(self.__next)})"
#End ADT        

# ADT Stack
class Stack(ADT):
    
    def __init__(self, item=None):
        """Ein Stapel mit dem übergebenen Inhalt wird angelegt."""
        super().__init__(item)

    def top(self):
        """Der Inhalt des obersten Elementes wird zurückgegeben, das Element aber nicht entnommen."""
        if self.item is None:
            raise getItemException("No Item in this stack!")
        return self.item

    def pop(self):
        """Der Inhalt des obersten Elements wird zurückgegeben, das Element wird entnommen."""
        if self.item is None:
            raise getItemException("No item in this stack!")
        out = self.item
        if self._ADT__next is None:
            self._ADT__item = None
        else:
            self.item = self._ADT__next.top()
            self._ADT__next = self._ADT__next._ADT__next
        return out

    def push(self, item):
        """Ein neues Element mit dem übergebenen Inhalt wird auf den Stapel gelegt."""
        if self.isEmpty():
            self.item = item
        elif isinstance(item, type(self.item)):
            stack = Stack(self.item)
            stack._ADT__next = self._ADT__next
            self.item = item
            self._ADT__next = stack
        else:
            raise TypeError('Type of item is ', type(item), ', but must be ', type(self._ADT__item))
#End Stack

#ADT Queue
class Queue(ADT):

    def __init__(self, item=None):
        """Eine Warteschlange wird mit dem übergebenen Inhalt angelegt."""
        super().__init__(item) 
    
    def head(self):
        """Der Inhalt des vordersten Elementes wird zurückgegeben, das Element wird nicht entnommen"""
        if self.item is None:
            raise getItemException("No item in this Queue!")
        return self.item
    
    def dequeue(self):
        """Der Inhalt des vordersten Elements wird entnommen und das Element wird entfernt"""
        if self.item is None:
            raise getItemException("No item in this Queue!")
        out = self.item
        if self._ADT__next is None:
            self._ADT__item = None
        else:
            self.item = self._ADT__next.head()
            self._ADT__next = self._ADT__next._ADT__next
        return out
    
    def enqueue(self, item):
        """Ein neues Element wird mit dem übergebenen Inhalt am Ender der Schlange angefügt"""
        if self.isEmpty():
            self.item=item
        elif not isinstance(item, type(self.item)):
            raise TypeError('Type of item is ', type(item), ', but must be ', type(self._ADT__item))
        elif self._ADT__next is None:
            self._ADT__next = Queue(item)
        else:
            self._ADT__next.enqueue(item)
#End Queue

#ADT DynArray
class DynArray(ADT):

    def __init__(self, item = None):
        """Ein neues dynamisches Array wird mit dem übergebenen Inhalt angelegt"""
        super().__init__(item)
        self.__prev = None
    
    def append(self, item):
        """Ein neues Element mit dem übergebenen Inhalt wird am Ende der dynamischen Reihung angefügt"""
        if self.isEmpty():
            self.item = item
        elif not isinstance(item, type(self.item)):
            raise TypeError('Type of item is ', type(item), ', but must be ', type(self._ADT__item))
        elif self._ADT__next is None:
            new = DynArray(item)
            new.__prev = self
            self._ADT__next = new
        else:
            self._ADT__next.append(item)

    def getItem(self, index:int = 0):
        """Der Inhalt des Elementes an der Position 'index' wird zurückgegeben"""
        if index < 0 or not isinstance(index, int):
            raise IndexError('Index must be a positiv Integer')
        elif index >= len(self):
            raise IndexError('Index out of bound')
        elif index==0:
            return self.item
        else:
            return self._ADT__next.getItem(index-1)

    def insertAt(self, item, index:int=0):
        """Ein neues Element mit dem übergebenen Inhalt wird an der Position 'index' in der dynamischen Reihung eingefügt. Das Element, dass sich vorher an dieser Position befunden hat, und alle nachfolgenden werden nach hinten verschoben. Entspricht der Wert von 'index' der Länge des dynamischen Arrays, so wird ein neues Element am Ende des dynamischen Arrays angefügt."""
        if index < 0 or not isinstance(index, int):
            raise IndexError('Index must be a positiv Integer')
        elif index == len(self):
            self.append(item)
        elif index > len(self):
            raise IndexError('Index out of bound')
        elif index==0:
            new = DynArray(self.item)
            self.item = item
            if self._ADT__next is not None:
                new._ADT__next = self._ADT__next
                new._ADT__next.__prev = new
            self._ADT__next = new
            new.__prev = self
        else:
            self._ADT__next.insertAt(item, index-1)

    def setItem(self, item, index:int=0):
        """Der Inhalt des Elementes an der Position 'index' wird durch den übergebenen Inhalt ersetzt"""
        if self.isEmpty():
            self._ADT__item = item
            return
        elif index < 0 or not isinstance(index, int):
            raise IndexError('Index must be a positiv Integer')
        elif index >= len(self):
            raise IndexError('Index out of bound')
        elif index == 0:
            self.item = item
            return
        else:
            self._ADT__next.setItem(item, index-1)

    def delete(self, index:int = 0):
        """Das Element an der Position 'index' wird entfernt, alle nachfolgenden Elemente werden um einen nach vorne geschoben."""
        if index < 0 or not isinstance(index, int):
            raise IndexError('Index must be a positiv Integer')
        elif index >= len(self):
            raise IndexError('Index out of bound')
        elif self.isEmpty():
            raise getItemException('DynArray is Empty')
        elif index == 0:
            out = self.item
            if self._ADT__next is None and self.__prev is None:
                self._ADT__item = None
            elif self.__prev is None:
               self.item = self._ADT__next.item
               if self._ADT__next._ADT__next is not None:
                   self._ADT__next._ADT__next.__prev = self
                   self._ADT__next = self._ADT__next._ADT__next
               else:
                   self._ADT__next = None
            elif self._ADT__next is None:
                self.__prev._ADT__next = None
            else:
                self.__prev._ADT__next = self._ADT__next
                self._ADT__next.__prev = self.__prev
            return out
        else:
            self._ADT__next.delete(index-1)

    def getLength(self):
        """Die Anzahl der Elemente der dynamischen Reihung wird zurückgegeben"""
        return len(self)
#End DynArray

#BinTree
class BinTree():
    def __init__(self, item = None, left = None, right = None):
        """Ein Baum wird erzeugt. Der Baum besitzt keine Teilbäume. Der Inhaltswert der Wurzel ist leer oder enthält den übergebenen Inhalt. Der linke bzw. rechte Teilbaum kann auch übergeben werden."""
        self.__item = item
        self.__itemType = None
        if self.__item is not None:
            self.__itemType = type(self.__item)
        self.__left = left
        self.__right = right
        
    def isEmpty(self):
        """Wenn der Baum keine Teilbäume besitzt und der Inhalt leer ist, die Wurzel des Baums also leer ist, wird der Wert wahr zurückgegeben, sonst der Wert falsch."""
        return self.__item is None and self.__left is None and self.__right is None
    
    def isLeaf(self):
        """Wenn der Baum keine Teilbäume besitzt und der Inhalt nicht leer ist, die Wurzel des Baums also ein Blatt ist, wird der Wert wahr zurückgegeben, sonst der Wert falsch."""
        return self.__item is not None and self.__left is None and self.__right is None
    
    @property
    def item(self):
        #return self.__item
        pass
    def getItem(self):
        """Die Operation gibt den Inhaltswert der Wurzel des Baums zurück."""
        return self.__item
    @item.setter
    def item(self):
        pass
    def setItem(self, item):
        """Die Wurzel des Baums erhält den übergebenen Inhalt als Wert."""
        if item is None:
            raise TypeError('item must have a value')
        if self.__item is None:
            self.__itemType = type(item)
        if isinstance(item, self.__itemType):
            self.__item = item
        else:
            raise TypeError('type missmatch')   
    def hasItem(self):
        """Wenn die Wurzel des Baums einen Inhaltswert besitzt, wird der Wert wahr zurückgegeben, sonst der Wert falsch."""
        return self.__item is not None
    def deleteItem(self):
        """Die Operation löscht den Inhaltswert der Wurzel des Baums."""
        self.__item = None
    
    @property
    def itemType(self):
        return self.__itemType
    @itemType.setter
    def itemType():
        pass
           
    @property
    def left(self):
        #return self.__left
        pass
    def getLeft(self):
        """Die Operation gibt den linken Teilbaum zurück."""
        return self.__left
    @left.setter
    def left(self):
        pass
    def setLeft(self, left):
        """Der übergebene Baum wird als linker Teilbaum gesetzt."""
        if not isinstance(left, type(self)):
            raise TypeError('left must be of type ', type(self))
        if left.itemType != self.itemType:
            raise TypeError('item of left must be of type ', self.itemType)
        else:
            self.__left = left  
    def hasLeft(self):
        """Wenn der Baum einen linken Teilbaum besitzt, wird der Wert wahr zurückgegeben, sonst der Wert falsch."""
        return self.__left is not None   
    def deleteLeft(self):
        """Die Operation löscht den linken Teilbaum."""
        self.__left = None
    
    @property
    def right(self):
        pass
    def getRight(self):
        """Die Operation gibt den rechten Teilbaum zurück."""
        return self.__right
    @right.setter
    def right():
        pass
    def setRight(self, right):
        """Der übergebene Baum wird als rechter Teilbaum gesetzt."""
        if not isinstance(right, type(self)):
            raise TypeError('right must be of type', type(self))
        if right.itemType != self.itemType:
            raise TypeError('item of right must be of type ', self.itemType)
        else:
            self.__right = right
    def hasRight(self):
        """Wenn der Baum einen rechten Teilbaum besitzt, wird der Wert wahr zurückgegeben, sonst der Wert falsch."""
        return self.__right is not None
    def deleteRight(self):
        """Die Operation löscht den rechten Teilbaum."""
        self.__right = None
        
    #zusätzliche Methoden
    def preorder(self):
        """Gibt den Inhalt des Baumes als eine Liste in preorder aus."""
        preList = list()
        if self.hasItem():
            preList.append(self.getItem())
        if self.hasLeft():
            preList += self.__left.preorder()
        if self.hasRight():
            preList += self.__right.preorder()
        return preList
    
    def inorder(self):
        """Gibt den Inhalt des Baumes als eine Liste in inorder aus."""
        inList = list()
        if self.hasLeft():
            inList += self.__left.inorder()
        if self.hasItem():
            inList.append(self.getItem())
        if self.hasRight():
            inList += self.__right.inorder()
        return inList
            
    def postorder(self):
        """Gibt den Inhalt des Baumes als eine Liste in postorder aus."""
        postList = list()
        if self.hasLeft():
            postList += self.__left.postorder()
        if self.hasRight():
            postList += self.__right.postorder()
        if self.hasItem():
            postList.append(self.getItem())
        return postList
    
    def levelorder(self):
        """Gibt eine Liste mit der Anzahl der Elemente an Position 0 und den Inhalt des Baumes in levelorder aus."""
        counter = 0
        levelList = list()
        queue=Queue(self)
        while not queue.isEmpty():
            knot = queue.dequeue()
            if knot.hasItem():
                levelList.append(knot.getItem())
                counter += 1
            if knot.hasLeft():
                queue.enqueue(knot.getLeft())
            if knot.hasRight():
                queue.enqueue(knot.getRight())
        levelList.insert(0, counter)
        return levelList
    
    def __len__(self):
        """Gibt die Anzahl der Elemente aus."""
        return self.levelorder()[0]
    
#End BinTree