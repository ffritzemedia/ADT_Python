class wrongTypeException():
    pass

#Start BinTree
class BinTree():
    """Binärbaum gem. 'Ergänzende Hinweise zum Kerncurriculum INFORMATIK
für die gymnasiale Oberstufe am Gymnasium, an der Gesamtschule sowie
für das Kolleg'. Der Inhaltstyp der Knoten ist generisch und kann bei der Initialisierung frei gewählt, dann aber nicht mehr geändert werden."""
    class Tree():
        #Start Tree
        def __init__(self, item = None, left = None, right = None, prev = None):
            """Ein Baum wird erzeugt. Der Baum besitzt keine Teilbäume. Der Inhaltswert der Wurzel ist leer oder enthält den übergebenen Inhalt."""
            self.__item = item
            self.__left = left
            self.__right = right
            self.__prev = prev
        
        @property
        def item(self):
           return self.__item
        @item.setter
        def item(self, item = None):
            if self.__item is None or isinstance(item, type(self.__item)):
                self.__item = item
            else:
                raise wrongTypeException('Type of item is ', type(item), ', but needs to be ', type(self.__item))
        
        @property
        def left(self):
            return self.__left
        @left.setter
        def left(self, left = None):
            if left is None or isinstance(left, type(self)):
                self.__left = left
            else:
                raise wrongTypeException
        
        @property
        def right(self):
            return self.__right
        @right.setter
        def right(self, right = None):
            if right is None or isinstance(right, type(self)):
                self.__right = right
            else:
                raise wrongTypeException
             
        @property
        def prev(self):
            return self.__prev
        @prev.setter
        def left(self, prev = None):
            if prev is None or isinstance(prev, type(self)):
                self.__prev = prev
            else:
                raise wrongTypeException
        
        def isEmpty(self):
            return self.__item is None and self._left is None and self.__right is None
        
        def preorder(self):
            preorder = list()
            if self.item is not None:
                preorder.append(self.item)
            if self.left is not None:
                preorder += self.left.preorder()
            if self.right is not None:
                preorder += self.right.preorder()
            return preorder
        
        def inorder(self):
            inorder = list()
            if self.left is not None:
                inorder += self.left.inorder()
            if self.item is not None:
                inorder.append(self.item)
            if self.right is not None:
                inorder += self.right.inorder()
            return inorder
        
        def postorder(self):
            postorder = list()
            if self.left is not None:
                postorder += self.left.postorder()
            if self.right is not None:
                postorder += self.right.postorder()
            if self.item is not None:
                postorder.append(self.item)
            return postorder
        
        def levelorder(self):
            levelorder = list()
            queue = list()
            queue.append(self)
            while queue:
                knot = queue.pop(0)
                if knot.item is not None:
                    levelorder.append(knot.item)
                if knot.left is not None:
                    queue.append(knot.left)
                if knot.right is not None:
                    queue.append(knot.right)
            return levelorder
    #Ende Tree
    
    #Klasse BinTree
    def __init__(self, item = None, left = None, right = None, prev = None):
        """Ein Baum wird erzeugt. Der Baum besitzt keine Teilbäume. Der Inhaltswert der Wurzel ist leer oder enthält den übergebenen Inhalt."""
        self.__root = self.Tree(item, left, right, prev)
        self.__itemType = type(item)
    
    @property
    def root(self):
        pass
    @root.setter
    def root(self, root):
        pass
    
    @property
    def itemType(self):
        return self.__itemType
    @itemType.setter
    def itemType(self):
        pass
    
    def isLeaf(self):
        """Wenn der Baum keine Teilbäume besitzt, die Wurzel des Baums also ein Blatt ist, wird der Wert wahr zurückgegeben, sonst der Wert falsch."""
        return self.__root.left is None and self.__root.right is None
            
    def hasItem(self):
        """Wenn die Wurzel des Baums einen Inhaltswert besitzt, wird der Wert wahr zurückgegeben, sonst der Wert falsch."""
        return not self.__root.item is None
    
    def getItem(self):
        """Die Operation gibt den Inhaltswert der Wurzel des Baums zurück."""
        return self.__root.item
    
    def setItem(self, item):
        """Die Wurzel des Baums erhält den übergebenen Inhalt als Wert."""
        if self.__itemType is type(None):
            self.__itemType = type(item)
        if isinstance(item, self.__itemType):
            self.__root.item = item
        else:
            raise wrongTypeException
        
    def deleteItem(self):
        """Die Operation löscht den Inhaltswert der Wurzel des Baums."""
        self.__root._Tree__item = None
    
    def hasLeft(self):
        """Wenn der Baum einen linken Teilbaum besitzt, wird der Wert wahr zurückgegeben, sonst der Wert falsch."""
        return self.__root.left is not None
    
    def getLeft(self):
        """Die Operation gibt den linken Teilbaum zurück."""
        return self.__root.left
    
    def setLeft(self, item):
        """Der übergebene Inhalt wird als linker Teilbaum gesetzt."""
        if self.__itemType is type(None):
            self.__itemType = type(item)
        if isinstance(item, self.__itemType):
            self.__root.left = self.Tree(item)
            self.__root.left.__prev = self.__root
        else:
            raise wrongTypeException
        
    def deleteLeft(self):
        """Die Operation löscht den linken Teilbaum."""
        self.__root._Tree__left = None
    
    def hasRight(self):
        """Wenn der Baum einen rechten Teilbaum besitzt, wird der Wert wahr zurückgegeben, sonst der Wert falsch."""
        return self.__root.right is not None
        
    def getRight(self):
        """Die Operation gibt den rechten Teilbaum zurück."""
        return self.__root.right
    
    def setRight(self, item):
        """Der übergebene Baum wird als rechter Teilbaum gesetzt."""
        if self.__itemType is type(None):
            self.__itemType = type(item)
        if isinstance(item, self.__itemType):
            self.__root.right = self.Tree(item)
            self.__root.right.__prev = self.__root
        else:
            raise wrongTypeException
        
    def deleteRight(self):
        """Die Operation löscht den rechten Teilbaum."""
        self.__root._Tree__right = None
        
    def preorder(self):
        """Traversiert den Baum in 'preorder' und gibt die Inhaltswerte in einer Liste zurück"""
        return self.__root.preorder()
    
    def inorder(self):
        """Traversiert den Baum in 'inorder' und gibt die Inhaltswerte in einer Liste zurück"""
        return self.__root.inorder()
    
    def postorder(self):
        """Traversiert den Baum in 'postorder' und gibt die Inhaltswerte in einer Liste zurück"""
        return self.__root.postorder()
    
    def levelorder(self):
        """Traversiert den Baum in 'levelorder' und gibt die Inhaltswerte in einer Liste zurück"""
        return self.__root.levelorder()
#Ende BinTree

#Anfang Klasse SearchTree        
class SearchTree(BinTree):
    def __init__(self, item=None, prev=None):
        super().__init__(item, None, None, prev)
        #self.__root = BinTree(item, None, None, prev)
    
    def addItem(self, item):
        if not self.hasItem():
            self.setItem(item)
        elif item < self.getItem():
            if self.hasLeft():
                self.getLeft().addItem(item)
            else:
                self.setLeft(item)
        elif item > self.getItem():
            if self.hasRight():
                self.getRight().addItem(item)
            else:
                self.setRight(item)
        else:
            raise Exception("Item exists already")
                
    def contains(self, item):
        if not isinstance(item, self.itemType):
            raise wrongTypeException('contains can onlx be used with the same item type')
        elif item == self.getItem():
            return True
        elif self.hasLeft() and item < self.getItem():
            return self.getLeft.contains(item)
        elif self.hasRight() and item > self.getItem():
            return self.getRight().contains(item)
        else:
            return False
        
    
        
#Ende SearchTree