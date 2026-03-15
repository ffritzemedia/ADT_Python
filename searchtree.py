from adt import BinTree

class AccessForbidden(Exception):
    pass

class SearchTree(BinTree):
    
    def __init__(self, item = None, left=None, right=None, prev = None):
        if item is None or not self.isComparable(item):
            raise TypeError('item must be comparable')
        super().__init__(item, left, right)
        self.__prev = prev
    
    @staticmethod
    def isComparable(x):
        try:
            x<x
            return True
        except TypeError:
            return False
    
    #Verbotene Methoden aus der Klasse BinTree
    def setLeft(self):
        raise AccessForbidden('Method not allowed in Class', type(self))
    def setRight(self):
        raise AccessForbidden('Method not allowed in Class', type(self))
    def setItem(self):
        raise AccessForbidden('Method not allowed in Class', type(self))
    def deleteLeft(self):
        raise AccessForbidden('Method not allowed in Class', type(self))
    def deleteRight(self):
        raise AccessForbidden('Method not allowed in Class', type(self))

    #Überschriebene Methoden
    def deleteItem(self, item):
        pass

    #Methoden für die Klasse SearchTree
    def addItem(self, item):
        if item is None or not self.isComparable(item):
            raise TypeError('item must not be None and comparable')
        if self.isEmpty():
            self._BinTree__itemType = type(item)
            self._BinTree__item = item
            return True
        if not isinstance(item, self._BinTree__itemType):
            raise TypeError('item must be type ', self._BinTree__itemType)
        elif item == self.getItem():
            print('item exists already')
            return False
        elif item < self.getItem():
            if self.hasLeft():
                return self._BinTree__left.addItem(item)
            else:
                self._BinTree__left = SearchTree(item, None, None, self)
                return True
        elif item > self.getItem():
            if self.hasRight():
                return self._BinTree__right.addItem(item)
            else:
                self._BinTree__right = SearchTree(item, None, None, self)
        return False
    
    def deleteKnot(self):
        pass

    def contains(self, item):
        if item is None or not self.isComparable(item):
            raise TypeError('item must not be None and comparable')
        if self.isEmpty():
            return False
        if item == self.getItem():
            return True
        elif item < self.getItem():
            if self.hasLeft():
                return self._BinTree__left.contains(item)
            else:
                return False
        elif item > self.getItem():
            if self.hasRight():
                return self._BinTree__right.contains(item)
            else:
                return False
        return False

    def getSubtree(self, item):
        if item is None or not self.isComparable(item):
            raise TypeError('item must not be None and comparable')
        if self.isEmpty():
            return None
        if item == self.getItem():
            return self
        elif item < self.getItem():
            if self.hasLeft():
                return self._BinTree__left.getSubtree(item)
            else:
                return None
        elif item > self.getItem():
            if self.hasRight():
                return self._BinTree__right.getSubtree(item)
            else:
                return None
        return None
