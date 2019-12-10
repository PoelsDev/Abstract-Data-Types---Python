from Bestelling import Bestelling
from BinarySearchTree import BinarySearchTree
from DoubleLinkedCircularChain import DoubleLinkedCircularChain
from DoubleLinkNode import DoubleLinkNode
from Node import Node
from sQueue import Queue
from Stack import Stack
from TreeNode import TreeNode
from Werknemer import Werknemer
from TimeDelta import TimeDelta

# Hieronder staat de verouderde implementatie van opdracht 1
print("CHOCOLADEBAR - PROTOTYPE")
print("-"*50)

# 1
A = Werknemer(1,"Bart", "Janssens", 10)
print("1. Werknemer A is gemaakt met een workload van 10!")
chain1 = DoubleLinkedCircularChain()
print("Een gelinkte ketting werd gemaakt!")
chain1.insert(0, A)
print("Werknemer A is toegevoegd aan de ketting!")
print()

# 2
stack1 = Stack()
print("2.Een nieuwe stack is aangemaakt: 1.")
stack1.push(A)
print("Werknemer A is gepusht op de stack!")
print()

# 3
B = Werknemer(2, "Peter", "Devos", 3)
print("3. Werkenemer B is gemaakt met een workload van 3.")
chain1.insert(1, B)
print("Werknemer B is toegevoegd aan de ketting!")
print()

# 4
stack1.push(B)
print("4. Werknemer B is gepusht op de stack.")
print()

# 5
b1 = Bestelling(5, 1, 0, 1, False)
print("5. Een eerste bestelling is gemaakt met 5 credits.")
print()

# 6
queue1 = Queue(10)
print("6. Een queue met lengte 10 werd aangemaakt.")
queue1.enqueue(b1)
print("De eerste bestelling werd aan de queue toegevoegd.")
print()

# 7
b2 = Bestelling(8, 2, 1, 2, False)
print("7. Een tweede bestelling werd aangemaakt met 8 credits.")
print()

# 8
queue1.enqueue(b2)
print("8. De tweede bestelling werd toegevoegd aan de queue.")
print()

# 9
clock = TimeDelta()
clock.TimeUp()
clock.TimeUp()
print("9. De tijd staat nu op 2.")
print()

# 10
print(queue1.getFront())
currentBestelling1 = queue1.getFront()
queue1.dequeue()
print("10. De eerste bestelling werd gelezen.")
print()

# 11
currentWerknemer1 = stack1.pop()[0]
print(currentWerknemer1)
print("11. De eerste werknemer werd gelezen uit de stack.")
print()

# 12
currentWerknemer1.giveOrder(currentBestelling1)
print("12. De bestelling is aan de eerste werknemer uit de stack gegeven.")
print()

# 13
print(queue1.getFront())
currentBestelling2 = queue1.getFront()
queue1.dequeue()
print("13. Bestelling 2 wordt nu uit de queue gelezen.")
print()

# 14
currentWerknemer2 = stack1.pop()[0]
print(currentWerknemer2)
print("14. De volgende werknemer is uit de stack gelezen.")
print()

# 15
currentWerknemer2.giveOrder(currentBestelling2)
print("15. De tweede bestelling is aan de tweede werknemer van de stack gegeven.")
print()

# 16
clock.TimeUp()
clock.TimeUp()
print("De tijd is net met 2 gestegen.")
print()

# 17
if (currentWerknemer1.workload-currentWerknemer1.currentBestelling.credits) <= 0:
    print("17-18: De werknemer is klaar.")
    currentWerknemer1.currentBestelling = None
    stack1.push(currentWerknemer1)
    print("De werknemer (nr.2 van de stack) gaat terug op de stack.")
    bestelling_Tree = BinarySearchTree()
    print("Een binaire zoekboom werd aangemaakt.")
    bestelling_Tree.searchTreeInsert(currentBestelling1)
    print("Bestelling 1 werd toegevoegd aan de binaire zoekboom.")
else:
    print("17-18: De werknemer (nr.1 van de stack) is nog niet klaar.")

print()

if (currentWerknemer2.workload-currentWerknemer2.currentBestelling.credits) <= 0:
    print("17-18: De werknemer is klaar.")
    currentWerknemer2.currentBestelling = None
    stack1.push(currentWerknemer2)
    print("De werknemer (nr.2 van de stack) gaat terug op de stack.")
    bestelling_Tree.searchTreeInsert(currentBestelling2)
    print("Bestelling 2 werd toegevoegd aan de binaire zoekboom.")
else:
    print("17-18: De werknemer (nr.2 van de stack) is nog niet klaar.")

print()

# 19
clock.TimeUp()
clock.TimeUp()
print("De tijd is net met 2 verhoogd.")
print()

# 20
if (currentWerknemer2.workload-(2*currentWerknemer2.currentBestelling.credits)) <= 0:
    print("20-21: De werknemer is klaar.")
    currentWerknemer2.currentBestelling = None
    stack1.push(currentWerknemer1)
    print("De werknemer (nr.2 van de stack) gaat terug op de stack.")
    bestelling_Tree.searchTreeInsert(currentBestelling2)
    print("Bestelling 2 werd toegevoegd aan de binaire zoekboom.")
else:
    print("20-21: De werknemer (nr.2 van de stack) is nog niet klaar.")

print()

#EXTRA
print("Inorder Traversal van de reeds gemaakte binaire boom:")
bestelling_Tree.inorderTraverse()
print()
V = Werknemer(3, "Tibo", "yeet", 8)
chain1.insert(2, V)
print(chain1.retrieve(0)[0].value)
print(chain1.retrieve(1)[0].value)
print(chain1.retrieve(2)[0].value)
chain1.sort()
print()
print(chain1.retrieve(0)[0].value)
print(chain1.retrieve(1)[0].value)
print(chain1.retrieve(2)[0].value)

