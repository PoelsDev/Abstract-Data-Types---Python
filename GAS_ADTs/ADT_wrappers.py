from BinarySearchTree import BinarySearchTree
from DoubleLinkedCircularChain import DoubleLinkedCircularChain
from sQueue import Queue
from Stack import Stack
from TwoThreeFourTree import TwoThreeFourTree


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

    def tablePrint(self, filename):
        return self.bst.toDot(filename)


class ChainTableWrapper:
    def __init__(self):
        self.chain = DoubleLinkedCircularChain()

    def tableInsert(self, index, newItem):
        return self.chain.insert(index, newItem)

    def tableDelete(self, key):
        indexForKey = self.chain.getIndexForKey()
        return self.chain.delete(indexForKey)

    def tableRetrieve(self, searchKey):
        return self.chain.retrieve(searchKey)

    def tableIsEmpty(self):
        return self.chain.isEmpty()

    def tableLength(self):
        return self.chain.getLength()
    
    def tableTraverse(self):
        self.chain.sort()
        return self.chain.traverse()

    def tablePrint(self, filename):
        return self.chain.toDot(filename)


class QueueTableWrapper:
    def __init__(self, size):
        self.queue = Queue(size)

    def tableInsert(self, newItem):
        return self.queue.enqueue(newItem)

    def tableDelete(self):
        return self.queue.dequeue()

    def tableIsEmpty(self):
        return self.queue.isEmpty()

    def tableTraverse(self):
        return self.queue.traverse()

    def tablePrint(self, filename):
        return self.queue.toDot(filename)

class StackTableWrapper:
    def __init__(self):
        self.stack = Stack()

    def tableInsert(self, newItem):
        return self.stack.push(newItem)

    def tableDelete(self):
        return self.stack.pop()

    def tableIsEmpty(self):
        return self.stack.isEmpty()

    def tableTraverse(self):
        return self.stack.traverse()

    def tablePrint(self, filename):
        return self.stack.toDot(filename)


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

    def tablePrint(self, filename):
        return self.TwoThreeFour.toDot(filename)
