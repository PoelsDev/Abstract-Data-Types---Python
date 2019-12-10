# from Bestelling import Bestelling
# from BinarySearchTree import BinarySearchTree
# from DoubleLinkedCircularChain import DoubleLinkedCircularChain
# from DoubleLinkNode import DoubleLinkNode
# from Node import Node
# from sQueue import Queue
# from Stack import Stack
# from TreeNode import TreeNode
# from Werknemer import Werknemer
# from TimeDelta import TimeDelta
from InputReader import readInput
# from TwoThreeFourTree import TwoThreeFourTree
# from TwoThreeFourNode import TwoThreeFourNode
# from DummyObject import DummyObject
# import os
#
# # # Dit is een extra test voor mezelf en mag genegeerd worden.
# # print("CHOCOLADEBAR - PROTOTYPE")
# # print("-"*50)
# #
# # # 1
# # A = Werknemer(1,"Bart", "Janssens", 10)
# # print("1. Werknemer A is gemaakt met een workload van 10!")
# # chain1 = DoubleLinkedCircularChain()
# # print("Een gelinkte ketting werd gemaakt!")
# # chain1.insert(0, A)
# # print("Werknemer A is toegevoegd aan de ketting!")
# # print()
# #
# # # 2
# # stack1 = Stack()
# # print("2.Een nieuwe stack is aangemaakt: 1.")
# # stack1.push(A)
# # print("Werknemer A is gepusht op de stack!")
# # print()
# #
# # # 3
# # B = Werknemer(2, "Peter", "Devos", 3)
# # chain1.insert(1, B)
# # print()
# #
# # # EXTRA
# # V = Werknemer(3, "Tibo", "yeet", 8)
# # chain1.insert(2, V)
# # print(chain1.retrieve(0)[0].value)
# # print(chain1.retrieve(1)[0].value)
# # print(chain1.retrieve(2)[0].value)
# # chain1.sort()
# # print()
# # print(chain1.retrieve(0)[0].value)
# # print(chain1.retrieve(1)[0].value)
# # print(chain1.retrieve(2)[0].value)
# # print()
# # chain1.delete(1)
# # print(chain1.retrieve(0)[0].value)
# # print(chain1.retrieve(1)[0].value)
# #
# # print()
# # b1 = Bestelling(5, 1, 0, 1, False)
# # A = Werknemer(1,"Bart", "Janssens", 10)
# # B = Werknemer(2, "Peter", "Devos", 3)
# # b2 = Bestelling(8, 2, 1, 2, False)
# # b3 = Bestelling(4, 4, 4, 4, False)
# # b4 = Bestelling(3, 2, 5, 2, False)
# # b5 = Bestelling(3, 1, 7, 1, False)
# # b6 = Bestelling(3, 1, 2, 1, False)
# # b7 = Bestelling(3, 1, -1, 1, False)
# # b8 = Bestelling(3, 1, 12, 1, False)
# # b9 = Bestelling(3, 1, 13, 1, False)
# #
# # t1 = BinarySearchTree()
# # t1.searchTreeInsert(b4)
# # t1.searchTreeInsert(b5)
# # t1.searchTreeInsert(B)
# # t1.searchTreeInsert(A)
# # t1.searchTreeInsert(b3)
# # t1.searchTreeInsert(b1)
# # t1.searchTreeInsert(b2)
# # t1.toDot("output.txt")
# #readInput("./input.txt")
#
#
# # ttf = TwoThreeFourTree()
# # ttf.insertItem(b4)
# # ttf.toDot("output.dot")
# #
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # ttf.insertItem(b5)
# # ttf.toDot("output.dot")
# #
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # ttf.insertItem(B)
# # ttf.toDot("output.dot")
# #
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # ttf.insertItem(b2)
# # ttf.toDot("output.dot")
# #
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # ttf.insertItem(A)
# # ttf.toDot("output.dot")
# #
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # ttf.insertItem(b3)
# # ttf.toDot("output.dot")
# #
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # ttf.insertItem(b1)
# # ttf.insertItem(b6)
# # ttf.insertItem(b7)
# # ttf.insertItem(b8)
# # ttf.insertItem(b9)
# # ttf.toDot("output.dot")
# #
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # print("TTF INORDER")
# # print(ttf.retrieveItem(9))
# # ttf.inorder()
# #
# # ttf.toDot("output.dot")
# #
# # os.system("dot -Tps output.dot -o dotOutput.ps")
#
# ttf = TwoThreeFourTree()
# ttf.insertItem(DummyObject(8))
# ttf.insertItem(DummyObject(4))
# ttf.insertItem(DummyObject(2))
# ttf.insertItem(DummyObject(6))
# ttf.insertItem(DummyObject(1))
# ttf.insertItem(DummyObject(3))
# ttf.insertItem(DummyObject(5))
# ttf.insertItem(DummyObject(7))
# ttf.insertItem(DummyObject(12))
# ttf.insertItem(DummyObject(10))
# ttf.insertItem(DummyObject(14))
# ttf.insertItem(DummyObject(9))
# ttf.insertItem(DummyObject(11))
# ttf.insertItem(DummyObject(13))
# ttf.insertItem(DummyObject(15))
#
#
# ttf.deleteItem(6)
# ttf.toDot("output.dot")
#
# os.system("dot -Tps output.dot -o dotOutput.ps")
# ttf.deleteItem(4)
# ttf.toDot("output.dot")
#
# os.system("dot -Tps output.dot -o dotOutput.ps")
# ttf.deleteItem(8)
# ttf.toDot("output.dot")
#
# os.system("dot -Tps output.dot -o dotOutput.ps")
# ttf.deleteItem(15)
# ttf.toDot("output.dot")
#
# os.system("dot -Tps output.dot -o dotOutput.ps")
# ttf.deleteItem(7)
#
# print("TTF INORDER")
# print(ttf.retrieveItem(9))
# ttf.inorder()
#
# ttf.toDot("output.dot")
#
# os.system("dot -Tps output.dot -o dotOutput.ps")
#
# chain = DoubleLinkedCircularChain()
# chain.insert(0, DummyObject(8))
# chain.insert(1, DummyObject(6))
# chain.insert(2, DummyObject(22))
# chain.insert(3, DummyObject(3))
# chain.insert(4, DummyObject(15))
# chain.insert(5, DummyObject(2))
# chain.insert(6, DummyObject(12))
# chain.insert(7, DummyObject(9))
# chain.delete(2)
# # chain.toDot("output.dot")
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# print("----------------------------")
# chain.traverse()
# chain.sort()
# print("----------------------------")
# chain.traverse()
# print("----------------------------")
# print("QUEUE")
# queue = Queue(8)
# queue.enqueue(DummyObject(8))
# queue.enqueue(DummyObject(6))
# queue.enqueue(DummyObject(22))
# queue.enqueue(DummyObject(3))
# queue.enqueue(DummyObject(4))
# queue.enqueue(DummyObject(14))
# queue.enqueue(DummyObject(9))
# queue.dequeue()
# queue.traverse()
# # queue.toDot("output.dot")
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# print("----------------------------")
# print("STACK")
# st = Stack()
# st.push(DummyObject(8))
# st.push(DummyObject(13))
# st.push(DummyObject(50))
# st.push(DummyObject(89))
# st.push(DummyObject(0))
# st.push(DummyObject(23))
# st.push(DummyObject(2))
# # st.traverse()
# # st.toDot("output.dot")
# # os.system("dot -Tps output.dot -o dotOutput.ps")

readInput("input.txt")

