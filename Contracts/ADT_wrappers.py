from BinarySearchTree import BinarySearchTree
from DoubleLinkedCircularChain import DoubleLinkedCircularChain
from sQueue import Queue
from Stack import Stack
from TwoThreeFourTree import TwoThreeFourTree

#TODO: 1 wrapper voor alle ADTs

class BSTTableWrapper:
    def __init__(self):
        self.bst = BinarySearchTree()

    def tableInsert(self, newItem):
        return self.bst.searchTreeInsert(newItem)

    def tableDelete(self, searchKey):
        return self.bst.searchTreeDelete(searchKey)

    def tableRetrieve(self, searchKey):
        return self.bst.searchTreeRetrieve(searchKey)

    def tableIsEmpty(self):
        return self.bst.isEmpty()

    def tableTraverse(self):
        return self.bst.inorderTraverse()


class ChainTableWrapper:
    def __init__(self):
        self.chain = DoubleLinkedCircularChain()

    def tableInsert(self, newItem):
        return self.chain.insert(newItem)

    def tableDelete(self, searchKey):
        return self.chain.delete(searchKey)

    def tableRetrieve(self, searchKey):
        return self.chain.retrieve(searchKey)

    def tableIsEmpty(self):
        return self.chain.isEmpty()

    def tableLength(self):
        return self.chain.getLength()
    
    def tableTraverse(self):
        pass
        # TODO: traverse

class QueueTableWrapper:
    def __init__(self):
        self.queue = Queue()

    def tableInsert(self, newItem):
        return self.queue.enqueue(newItem)

    def tableDelete(self, searchKey):
        return self.queue.dequeue(searchKey)

    def tableIsEmpty(self):
        return self.queue.isEmpty()

    def tableTraverse(self):
        pass
        # TODO: traverse


class StackTableWrapper:
    def __init__(self):
        self.stack = Stack()

    def tableInsert(self, newItem):
        return self.stack.push(newItem)

    def tableDelete(self, searchKey):
        return self.stack.pop(searchKey)

    def tableIsEmpty(self):
        return self.stack.isEmpty()

    def tableTraverse(self):
        pass
        # TODO: traverse


class TwoThreeFourTreeTableWrapper:
    def __init__(self):
        self.TwoThreeFour = TwoThreeFourTree()

    def tableInsert(self, newItem):
        return self.TwoThreeFour.insertItem(newItem)

    def tableDelete(self, searchKey):
        return self.TwoThreeFour.deleteItem(searchKey)

    def tableRetrieve(self, searchKey):
        return self.TwoThreeFour.retrieveItem(searchKey)

    def tableIsEmpty(self):
        return self.TwoThreeFour.isEmpty()

    def tableTraverse(self):
        return self.TwoThreeFour.inorder()
