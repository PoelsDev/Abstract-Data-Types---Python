from TwoThreeFourNode import TwoThreeFourNode
from random import randint
from copy import deepcopy

class TwoThreeFourTree:
    def __init__(self):
        self.root = None
        self.parent = None
        self.subtrees = [None] * 4

    def inorder(self):
        """
        +inorder(in tree:TwoThreeTree)
        Doorloopt de niet-lege 2-3-4 tree in volgorde van de keys.
        Pre-condities: geen.
        Post-condities: De boom wordt doorlopen in volgorde van de keys.
        """
        if not self.isEmpty():
            if self.getNodeAmount() == 1:
                if self.subtrees[0] is not None:
                    self.subtrees[0].inorder()
                print(self.root.keys[0])
                if self.subtrees[1] is not None:
                    self.subtrees[1].inorder()
            elif self.getNodeAmount() == 2:
                if self.subtrees[0] is not None:
                    self.subtrees[0].inorder()
                print(self.root.keys[0])
                if self.subtrees[1] is not None:
                    self.subtrees[1].inorder()
                print(self.root.keys[1])
                if self.subtrees[2] is not None:
                    self.subtrees[2].inorder()
            elif self.getNodeAmount() == 3:
                if self.subtrees[0] is not None:
                    self.subtrees[0].inorder()
                print(self.root.keys[0])
                if self.subtrees[1] is not None:
                    self.subtrees[1].inorder()
                print(self.root.keys[1])
                if self.subtrees[2] is not None:
                    self.subtrees[2].inorder()
                print(self.root.keys[2])
                if self.subtrees[3] is not None:
                    self.subtrees[3].inorder()

    def retrieveItem(self, searchKey):
        """
        +retrieveItem(in searchKey:KeyType, out:TreeItemType):boolean
        Als het item met de key (searchKey) zich bevindt in de boom zal dit item teruggegeven worden.
        :param searchKey: Zoeksleutel waarvoor een corresponderend item moet worden gevonden.
        :return: True of False op basis van het succes van de functie en het gevonden item (bij True)
        Pre-condities: De parameter searchKey moet een getKey()-functie ter beschikking hebben.
        Post-condities: Een item wordt teruggegeven uit de 2-3-4 tree.
        """
        if not self.isEmpty():
            if self.isLeaf():
                for n in self.root.keys:
                    if searchKey == n.getKey():
                        return True
            else:
                for n in self.root.keys:
                    if searchKey == n.getKey():
                        return True
                if self.getNodeAmount() == 1:
                    if searchKey < self.root.keys[0].getKey():
                        return self.subtrees[0].retrieveItem(searchKey)
                    else:
                        return self.subtrees[1].retrieveItem(searchKey)
                if self.getNodeAmount() == 2:
                    if searchKey < self.root.keys[0].getKey():
                        return self.subtrees[0].retrieveItem(searchKey)
                    elif self.root.keys[0].getKey() < searchKey < self.root.keys[1].getKey():
                        return self.subtrees[1].retrieveItem(searchKey)
                    elif searchKey > self.root.keys[1].getKey():
                        return self.subtrees[2].retrieveItem(searchKey)
                if self.getNodeAmount() == 3:
                    if searchKey < self.root.keys[0].getKey():
                        return self.subtrees[0].retrieveItem(searchKey)
                    elif self.root.keys[0].getKey() < searchKey < self.root.keys[1].getKey():
                        return self.subtrees[1].retrieveItem(searchKey)
                    elif self.root.keys[1].getKey() < searchKey < self.root.keys[2].getKey():
                        return self.subtrees[2].retrieveItem(searchKey)
                    elif searchKey > self.root.keys[2].getKey():
                        return self.subtrees[3].retrieveItem(searchKey)
        return False

    def getSubTrees(self):
        temp = deepcopy(self.subtrees)
        for i in range(0, temp.count(None)):
            temp.remove(None)

        return len(temp)

    def getSubTreeIndex(self, searchKey):
        if self.getNodeAmount() == 1:
            if self.root.keys[0].getKey() < searchKey:
                return 1
            else:
                return 0
        elif self.getNodeAmount() == 2:
            if self.root.keys[0].getKey() > searchKey:
                return 0
            elif self.root.keys[0].getKey() < searchKey < self.root.keys[1].getKey():
                return 1
            elif self.root.keys[1].getKey() < searchKey:
                return 2
        elif self.getNodeAmount() == 3:
            if self.root.keys[0].getKey() > searchKey:
                return 0
            elif self.root.keys[0].getKey() < searchKey < self.root.keys[1].getKey():
                return 1
            elif self.root.keys[1].getKey() < searchKey < self.root.keys[2].getKey():
                return 2
            elif self.root.keys[2].getKey() < searchKey:
                return 3

    def getNodeAmount(self):
        return len(self.root.keys)

    def isLeaf(self):
        if self.getSubTrees() == 0:
            return True
        return False

    def isRoot(self):
        if self.parent is None:
            return True
        return False

    def insertItem(self, newItem):
        """
        +insertItem(in newItem:TreeItemType)
        Voegt een item toe aan de 2-3-4 tree.
        :param newItem: Het toe te voegen item.
        Pre-condities: De parameter newItem moet een getKey()-functie ter beschikking hebben.
        Post-condities: Het item zal in de boom zijn toegevoegd.
        """
        if self.isEmpty():
            self.root = TwoThreeFourNode()
            self.root.keys.append(newItem)
        else:
            if self.isRoot():
                if self.isLeaf():
                    if self.getNodeAmount() < 3:
                        if self.getNodeAmount() == 1:
                            if self.root.keys[0].getKey() > newItem.getKey():
                                self.root.keys.insert(0, newItem)
                            else:
                                self.root.keys.append(newItem)
                        elif self.getNodeAmount() == 2:
                            if self.root.keys[0].getKey() > newItem.getKey():
                                self.root.keys.insert(0, newItem)
                            elif self.root.keys[0].getKey() < newItem.getKey() < self.root.keys[1].getKey():
                                self.root.keys.insert(1, newItem)
                            else:
                                self.root.keys.append(newItem)
                    elif self.getNodeAmount() == 3:
                        self.split()
                        self.subtrees[self.getSubTreeIndex(newItem.getKey())].insertItem(newItem)
                else:
                    if self.getNodeAmount() < 3:
                        index = self.getSubTreeIndex(newItem.getKey())
                        if self.subtrees[index].getNodeAmount() == 3:
                            self.subtrees[index].split()
                        self.subtrees[self.getSubTreeIndex(newItem.getKey())].insertItem(newItem)
                    else:
                        self.split()
                        index = self.getSubTreeIndex(newItem.getKey())
                        if self.subtrees[index].getNodeAmount() == 3:
                            self.subtrees[index].split()
                        self.subtrees[self.getSubTreeIndex(newItem.getKey())].insertItem(newItem)
            else:
                if self.isLeaf() is False:
                    index = self.getSubTreeIndex(newItem.getKey())
                    if self.subtrees[index].getNodeAmount() == 3:
                        self.subtrees[index].split()
                        self.subtrees[self.getSubTreeIndex(newItem.getKey())].insertItem(newItem)
                    else:
                        self.subtrees[self.getSubTreeIndex(newItem.getKey())].insertItem(newItem)
                else:
                    if self.getNodeAmount() < 3:
                        if self.getNodeAmount() == 1:
                            if self.root.keys[0].getKey() > newItem.getKey():
                                self.root.keys.insert(0, newItem)
                            else:
                                self.root.keys.append(newItem)
                        elif self.getNodeAmount() == 2:
                            if self.root.keys[0].getKey() > newItem.getKey():
                                self.root.keys.insert(0, newItem)
                            elif self.root.keys[0].getKey() < newItem.getKey() < self.root.keys[1].getKey():
                                self.root.keys.insert(1, newItem)
                            else:
                                self.root.keys.append(newItem)

    def split(self):
        """
        +split()
        Splitst de subboom waarin hij zich bevindt
        Pre-condities: geen
        Post-condities: De deelboom van aanroep zal gesplitst zijn.
        """
        if self.parent is None:
            temp = self.TreeCopy()
            self.root = temp.root
            self.subtrees = temp.subtrees
            for tree in self.subtrees:
                if tree is not None:
                    tree.parent = self
        else:
            if self.parent.getNodeAmount() < 3:
                if self.parent.getNodeAmount() == 1:
                    if self.parent.root.keys[0].getKey() > self.root.keys[1].getKey():
                        temp = self.TreeCopy()
                        self.parent.root.keys.insert(0, self.root.keys[1])
                        if self.parent.subtrees[1] is not None:
                            self.parent.subtrees[2] = self.parent.subtrees[1]
                        self.parent.subtrees[0] = temp.subtrees[0]
                        if self.parent.subtrees[0] is not None:
                            self.parent.subtrees[0].parent = self.parent
                        self.parent.subtrees[1] = temp.subtrees[1]
                        if self.parent.subtrees[1] is not None:
                            self.parent.subtrees[1].parent = self.parent
                    else:
                        temp = self.TreeCopy()
                        self.parent.root.keys.append(self.root.keys[1])
                        self.parent.subtrees[1] = temp.subtrees[0]
                        if self.parent.subtrees[1] is not None:
                            self.parent.subtrees[1].parent = self.parent
                        self.parent.subtrees[2] = temp.subtrees[1]
                        if self.parent.subtrees[2] is not None:
                            self.parent.subtrees[2].parent = self.parent
                elif self.parent.getNodeAmount() == 2:
                    if self.parent.root.keys[0].getKey() > self.root.keys[1].getKey():
                        temp = self.TreeCopy()
                        self.parent.root.keys.insert(0, self.root.keys[1])
                        if self.parent.subtrees[2] is not None:
                            self.parent.subtrees[3] = self.parent.subtrees[2]
                        if self.parent.subtrees[1] is not None:
                            self.parent.subtrees[2] = self.parent.subtrees[1]
                        self.parent.subtrees[0] = temp.subtrees[0]
                        if self.parent.subtrees[0] is not None:
                            self.parent.subtrees[0].parent = self.parent
                        self.parent.subtrees[1] = temp.subtrees[1]
                        if self.parent.subtrees[1] is not None:
                            self.parent.subtrees[1].parent = self.parent
                    elif self.parent.root.keys[0].getKey() < self.root.keys[1].getKey() < self.parent.root.keys[1].getKey():
                        temp = self.TreeCopy()
                        self.parent.root.keys.insert(1, self.root.keys[1])
                        if self.parent.subtrees[1] is not None:
                            self.parent.subtrees[3] = self.subtrees[1]
                        self.parent.subtrees[1] = temp.subtrees[0]
                        if self.parent.subtrees[1] is not None:
                            self.parent.subtrees[1].parent = self.parent
                        self.parent.subtrees[2] = temp.subtrees[1]
                        if self.parent.subtrees[2] is not None:
                            self.parent.subtrees[2].parent = self.parent
                    elif self.parent.root.keys[1].getKey() < self.root.keys[1].getKey():
                        temp = self.TreeCopy()
                        self.parent.root.keys.append(self.root.keys[1])
                        self.parent.subtrees[2] = temp.subtrees[0]
                        if self.parent.subtrees[2] is not None:
                            self.parent.subtrees[2].parent = self.parent
                        self.parent.subtrees[3] = temp.subtrees[1]
                        if self.parent.subtrees[3] is not None:
                            self.parent.subtrees[3].parent = self.parent

    def TreeCopy(self):
        temp = TwoThreeFourTree()
        temp.root = TwoThreeFourNode()
        temp.root.keys.append(self.root.keys[1])
        temp.subtrees[0] = TwoThreeFourTree()
        temp.subtrees[0].parent = temp
        temp.subtrees[0].root = TwoThreeFourNode()
        temp.subtrees[0].root.keys.append(self.root.keys[0])
        temp.subtrees[0].subtrees[0] = self.subtrees[0]
        if temp.subtrees[0].subtrees[0] is not None:
            temp.subtrees[0].subtrees[0].parent = temp.subtrees[0]
        temp.subtrees[0].subtrees[1] = self.subtrees[1]
        if temp.subtrees[0].subtrees[1] is not None:
            temp.subtrees[0].subtrees[1].parent = temp.subtrees[0]
        temp.subtrees[1] = TwoThreeFourTree()
        temp.subtrees[1].root = TwoThreeFourNode()
        temp.subtrees[1].root.keys.append(self.root.keys[2])
        temp.subtrees[1].parent = temp
        temp.subtrees[1].subtrees[0] = self.subtrees[2]
        if temp.subtrees[1].subtrees[0] is not None:
            temp.subtrees[1].subtrees[0].parent = temp.subtrees[1]
        temp.subtrees[1].subtrees[1] = self.subtrees[3]
        if temp.subtrees[1].subtrees[1] is not None:
            temp.subtrees[1].subtrees[1].parent = temp.subtrees[1]

        return temp

    def deleteItem(self, searchKey):
        """
        +deleteItem(in searchKey:KeyType):boolean
        Deze functie verwijdert een item op basis van searchKey als dit zich in de boom bevindt.
        True/False duiden aan of dit gelukt is of niet.
        :param searchKey: Het te verwijderen item (met getKey()-functie)
        :return: True/False: om aan te tonen of te verwijdering correct is gelukt of niet.
        Pre-condities: De parameter searchKey moet een getKey()-functie hebben.
        Post-condities: Als het te verwijderen item zich bevond in de 2-3-4 tree, is het nu verwijderd.
        """
        if not self.isEmpty():
            if self.retrieveItem(searchKey) is True:
                if not self.isRoot():
                    if self.isLeaf():
                        if self.getNodeAmount() == 1:
                            self.fix()
                        else:
                            for i in range(0, len(self.root.keys)):
                                if self.root.keys[i].getKey() == searchKey:
                                    index = i
                                    break
                            self.root.keys.remove(self.root.keys[i])
                    else:
                        if self.getNodeAmount() == 1:
                            self.fix()
                        found = False
                        for i in range(0, len(self.root.keys)):
                            if self.root.keys[i].getKey() == searchKey:
                                found = True
                        if found:
                            inorder = self.findInorder(searchKey)
                            # if inorder.getNodeAmount == 1:
                            #     inorder.fix()
                            index = None
                            for i in range(0, len(self.root.keys)):
                                if self.root.keys[i].getKey() == searchKey:
                                    index = i
                                    break
                            if index is not None:
                                temp = self.root.keys[index]
                                self.root.keys[index] = inorder.root.keys[0]
                                inorder.root.keys[0] = temp
                                inorder.root.keys.remove(inorder.root.keys[0])
                            else:
                                inorder.root.keys.remove(inorder.root.keys[0])
                        else:
                            index = self.getSubTreeIndex(searchKey)
                            if self.subtrees[index].getNodeAmount() == 1:
                                self.subtrees[index].fix()
                            self.subtrees[self.getSubTreeIndex(searchKey)].deleteItem(searchKey)
                else:
                    if self.isLeaf():
                        index = None
                        for i in range(0, len(self.root.keys)):
                            if self.root.keys[i].getKey() == searchKey:
                                index = i
                                break
                        del self.root.keys[index]
                    else:
                        found = False
                        for i in range(0, len(self.root.keys)):
                            if self.root.keys[i].getKey() == searchKey:
                                found = True
                        if found:
                            inorder = self.findInorder(searchKey)
                            # if inorder.getNodeAmount() == 1:
                            #     inorder.fix()
                            index = None
                            for i in range(0, len(self.root.keys)):
                                if self.root.keys[i].getKey() == searchKey:
                                    index = i
                                    break
                            temp = self.root.keys[index]
                            self.root.keys[index] = inorder.root.keys[0]
                            inorder.root.keys[0] = temp
                            inorder.root.keys.remove(inorder.root.keys[0])
                        else:
                            index = self.getSubTreeIndex(searchKey)
                            self.subtrees[index].deleteItem(searchKey)
            else:
                return False
        else:
            return False

    def findInorder(self, searchKey):
        temp = None
        index = None
        successor = None
        for i in range(0, len(self.root.keys)):
            if self.root.keys[i].getKey() == searchKey:
                index = i
                break

        if index == 0:
            temp = self.subtrees[1]
            if temp.getNodeAmount() == 1:
                temp.fix()
            while temp.isLeaf() is False:
                temp = temp.subtrees[0]
                # self.fix()
                if temp.getNodeAmount() == 1:
                    temp.fix()
            if temp.getNodeAmount() == 1:
                    temp.fix()
            successor = temp
        elif index == 1:
            temp = self.subtrees[2]
            if temp.getNodeAmount() == 1:
                temp.fix()
            # self.fix()
            while temp.isLeaf() is False:
                temp = temp.subtrees[0]
                # self.fix()
                if temp.getNodeAmount() == 1:
                    temp.fix()
            if temp.getNodeAmount() == 1:
                    temp.fix()
            successor = temp
        elif index == 2:
            temp = self.subtrees[3]
            if temp.getNodeAmount() == 1:
                temp.fix()
            # self.fix()
            while temp.isLeaf() is False:
                temp = temp.subtrees[0]
                if temp.getNodeAmount() == 1:
                    temp.fix()
                # self.fix()
            if temp.getNodeAmount() == 1:
                    temp.fix()
            successor = temp

        return successor

    def mergeNodes(self):
        index = self.parent.getSubTreeIndex(self.root.keys[0].getKey())
        if index == 0:
            temp = TwoThreeFourTree()
            temp.root = TwoThreeFourNode()
            temp.root.keys.append(self.parent.subtrees[0].keys[0])
            temp.root.keys.append(self.parent.root.keys[index])
            temp.root.keys.append(self.parent.subtrees[index+1].root.keys[0])
            temp.subtrees[0] = self.subtrees[0]
            if temp.subtrees[0] is not None:
                temp.subtrees[0].parent = temp
            temp.subtrees[1] = self.subtrees[1]
            if temp.subtrees[1] is not None:
                temp.subtrees[1].parent = temp
            temp.subtrees[2] = self.parent.subtrees[index+1].subtrees[0]
            if temp.subtrees[2] is not None:
                temp.subtrees[2].parent = temp
            temp.subtrees[3] = self.parent.subtrees[index+1].subtrees[1]
            if temp.subtrees[3] is not None:
                temp.subtrees[3].parent = temp
            if self.parent.isRoot() and self.parent.getNodeAmount() == 1:
                self.parent.root.keys.remove(self.parent.root.keys[0])
                self.parent.root = temp.root
                self.parent.subtrees = temp.subtrees
                for tree in self.parent.subtrees:
                    tree.parent = self.parent
                return True
            self.parent.root.keys.remove(self.parent.root.keys[0])
            del self.parent.subtrees[0]
            self.parent.subtrees.append(None)
            self.parent.subtrees[0] = temp
            temp.parent = self.parent
            return True
        else:
            temp = TwoThreeFourTree()
            temp.root = TwoThreeFourNode()
            temp.root.keys.append(self.parent.subtrees[index - 1].root.keys[len(self.parent.subtrees[index - 1].root.keys)-1])
            temp.root.keys.append(self.parent.root.keys[index-1])
            temp.root.keys.append(self.parent.subtrees[index].root.keys[0])
            temp.subtrees[0] = self.parent.subtrees[index -1].subtrees[0]
            if temp.subtrees[0] is not None:
                temp.subtrees[0].parent = temp
            temp.subtrees[1] = self.parent.subtrees[index -1].subtrees[1]
            if temp.subtrees[1] is not None:
                temp.subtrees[1].parent = temp
            temp.subtrees[2] = self.subtrees[0]
            if self.subtrees[2] is not None:
                temp.subtrees[2].parent = temp
            temp.subtrees[3] = self.subtrees[1]
            if self.subtrees[3] is not None:
                temp.subtrees[3].parent = temp
            if self.parent.isRoot() and self.parent.getNodeAmount() == 1:
                self.parent.root.keys.remove(self.parent.root.keys[index - 1])
                self.parent.root = temp.root
                self.parent.subtrees = temp.subtrees
                for tree in self.parent.subtrees:
                    tree.parent = self.parent
                return True
            self.parent.root.keys.remove(self.parent.root.keys[index - 1])
            del self.parent.subtrees[index]
            self.parent.subtrees.append(None)
            self.parent.subtrees[index - 1] = temp
            temp.parent = self.parent
            return True

    def redistributeNodes(self):
        position = self.parent.getSubTreeIndex(self.root.keys[0].getKey())
        siblingIndex = self.checkSibling(position)
        if siblingIndex[0] is not None:
            if siblingIndex[1] == 1:
                temp = self.parent.root.keys[position]
                self.root.keys.append(temp)
                self.parent.root.keys[position] = self.parent.subtrees[position+1].root.keys[0]
                self.parent.subtrees[position+1].root.keys.remove(self.parent.subtrees[position+1].root.keys[0])
                if self.parent.subtrees[position+1].subtrees[0] is not None:
                    self.parent.subtrees[position+1].subtrees[0].parent = self
                self.subtrees[2] = self.parent.subtrees[position+1].subtrees[0]
                siblingKeys = self.parent.subtrees[position+1].getNodeAmount()
                if siblingKeys == 1:
                    self.parent.subtrees[position+1].subtrees.remove(self.parent.subtrees[position+1].subtrees[0])
                    self.parent.subtrees[position+1].subtrees.append(None)
                elif siblingKeys == 2:
                    self.parent.subtrees[position+1].TwoSiblingShiftRightSibling()
                elif siblingKeys == 3:
                    self.parent.subtrees[position+1].ThreeSiblingShiftRightSibling()
                return True
            if siblingIndex[1] == 0:
                temp = self.parent.root.keys[position-1]
                self.root.keys.insert(0, temp)
                self.parent.root.keys[position-1] = self.parent.subtrees[position-1].root.keys[len(self.parent.subtrees[position-1].root.keys)-1]
                self.parent.subtrees[position-1].root.keys.remove(self.parent.subtrees[position-1].root.keys[len(self.parent.subtrees[position-1].root.keys)-1])
                self.subtrees[2] = self.subtrees[1]
                self.subtrees[1] = self.subtrees[0]
                if self.parent.subtrees[position-1].subtrees[self.parent.subtrees[position-1].getSubTrees()] is not None:
                    self.parent.subtrees[position-1].subtrees[self.parent.subtrees[position-1].getSubTrees()].parent = self
                self.subtrees[0] = self.parent.subtrees[position-1].subtrees[self.parent.subtrees[position-1].getSubTrees()]
                self.parent.subtrees[position-1].subtrees[self.parent.subtrees[position-1].getSubTrees()] = None
                return True
        else:
            return False

    def fix(self):
        if not self.isRoot():
            redis = self.redistributeNodes()
            if redis is True:
                return True
            else:
                self.mergeNodes()
                return True
            return True

    def checkSibling(self, position):
        if position == 0:
            siblingCheck = self.checkRightSibling(position)
            if siblingCheck[0] is True:
                return siblingCheck[1], 1
            else:
                return None, -1
        elif position == 1:
            siblingCheck1 = self.checkRightSibling(position)
            if siblingCheck1[0] is True:
                return siblingCheck1[1], 1
            siblingCheck2 = self.checkLeftSibling(position)
            if siblingCheck2[0] is True:
                return siblingCheck2[1], 0
            else:
                return None, None
        elif position == 2:
            siblingCheck1 = self.checkRightSibling(position)
            if siblingCheck1[0] is True:
                return siblingCheck1[1], 1
            siblingCheck2 = self.checkLeftSibling(position)
            if siblingCheck2 is True:
                return siblingCheck2[1], 0
            else:
                return None, None
        elif position == 3:
            siblingCheck = self.checkLeftSibling(position)
            if siblingCheck[0] is True:
                return siblingCheck[1], 0
            else:
                return None, None
        else:
            return None, None

    def checkRightSibling(self, position):
        if position == 0:
            if self.parent.subtrees[1] is not None:
                if self.parent.subtrees[1].getNodeAmount() > 1:
                    return True, 1
                else:
                    return False, None
            else:
                return False, None
        if position == 1:
            if self.parent.subtrees[2] is not None:
                if self.parent.subtrees[2].getNodeAmount() > 1:
                    return True, 2
                else:
                    return False, None
            else:
                return False, None
        if position == 2:
            if self.parent.subtrees[3] is not None:
                if self.parent.subtrees[3].getNodeAmount() > 1:
                    return True, 3
                else:
                    return False, None
            else:
                return False, None

    def checkLeftSibling(self, position):
        if position == 1:
            if self.parent.subtrees[0] is not None:
                if self.parent.subtrees[0].getNodeAmount() > 1:
                    return True, 0
                else:
                    return False, None
            else:
                return False, None
        if position == 2:
            if self.parent.subtrees[1] is not None:
                if self.parent.subtrees[1].getNodeAmount() > 1:
                    return True, 1
                else:
                    return False, None
            else:
                return False, None
        if position == 3:
            if self.subtrees[2] is not None:
                if self.parent.subtrees[2].getNodeAmount() > 1:
                    return True, 2
                else:
                    return False, None
            else:
                return False, None

    def TwoSiblingShiftRightSibling(self):
        self.subtrees[0] = self.subtrees[1]
        self.subtrees[1] = self.subtrees[2]
        self.subtrees[2] = None

    def ThreeSiblingShiftRightSibling(self):
        self.subtrees[0] = self.subtrees[1]
        self.subtrees[1] = self.subtrees[2]
        self.subtrees[2] = self.subtrees[3]
        self.subtrees[3] = None

    # def parentIsPredecessor(self, predecessor):
    #     if self.parent == predecessor:
    #         return True

    def isEmpty(self):
        """
        +isEmpty():boolean
        Geeft weer of de boom leeg is of niet.
        :return: True/False
        Pre-condities: geen.
        Post-condities: Er wordt weergegeven of de 2-3-4 tree leeg is of niet.
        """
        if self.root is None and self.parent is None:
            return True
        return False


    def generateDot(self):
        dot = ""
        link = "--"
        rand1 = str(randint(1,100))
        rand2 = str(randint(1,100))

        if not self.isEmpty():
            dot+=f"\nnode{rand1} [label={rand1}, style=invis]\n"
            dot+=f"node{rand2} [label={rand2}, style=invis]\n"
            dot+="\n"

            dot+="\""
            for i in range(0,len(self.root.keys)-1):
                dot+=f"{str(self.root.keys[i].getKey())} "
            dot+=str(self.root.keys[len(self.root.keys)-1].getKey()) + "\""

            if self.subtrees[0] is None:
                #dot+= f" {link} node{rand1} [style=invis]"
                pass
            else:
                dot+=f" {link} "
                dot+="\""
                for i in range(0,len(self.subtrees[0].root.keys)-1):
                    dot+=f"{str(self.subtrees[0].root.keys[i].getKey())} "
                dot+=str(self.subtrees[0].root.keys[len(self.subtrees[0].root.keys)-1].getKey()) + "\""

            dot += "\n"
            dot +="\""
            for i in range(0,len(self.root.keys)-1):
                dot+=f"{str(self.root.keys[i].getKey())} "
            dot+=str(self.root.keys[len(self.root.keys)-1].getKey()) + "\""

            if self.subtrees[1] is None:
                #dot+= f" {link} node{rand1} [style=invis]"
                pass
            else:
                dot+=f" {link} "
                dot+="\""
                for i in range(0,len(self.subtrees[1].root.keys)-1):
                    dot+=f"{str(self.subtrees[1].root.keys[i].getKey())} "
                dot+=str(self.subtrees[1].root.keys[len(self.subtrees[1].root.keys)-1].getKey()) + "\""

            dot += "\n"
            dot +="\""
            for i in range(0,len(self.root.keys)-1):
                dot+=f"{str(self.root.keys[i].getKey())} "
            dot+=str(self.root.keys[len(self.root.keys)-1].getKey()) + "\""

            if self.subtrees[2] is None:
                #dot+= f" {link} node{rand1} [style=invis]"
                pass
            else:
                dot+=f" {link} "
                dot+="\""
                for i in range(0,len(self.subtrees[2].root.keys)-1):
                    dot+=f"{str(self.subtrees[2].root.keys[i].getKey())} "
                dot+=str(self.subtrees[2].root.keys[len(self.subtrees[2].root.keys)-1].getKey()) + "\""

            dot += "\n"
            dot +="\""
            for i in range(0,len(self.root.keys)-1):
                dot+=f"{str(self.root.keys[i].getKey())} "
            dot+=str(self.root.keys[len(self.root.keys)-1].getKey()) + "\""

            if self.subtrees[3] is None:
                #dot+= f" {link} node{rand1} [style=invis]"
                pass
            else:
                dot+=f" {link} "
                dot+="\""
                for i in range(0,len(self.subtrees[3].root.keys)-1):
                    dot+=f"{str(self.subtrees[3].root.keys[i].getKey())} "
                dot+=str(self.subtrees[3].root.keys[len(self.subtrees[3].root.keys)-1].getKey()) + "\""

            dot+="\n"

            # recursieve stap
            if self.subtrees[0] is not None:
              dot += self.subtrees[0].generateDot()
            if self.subtrees[1] is not None:
                dot += self.subtrees[1].generateDot()
            if self.subtrees[2] is not None:
                dot += self.subtrees[2].generateDot()
            if self.subtrees[3] is not None:
                dot += self.subtrees[3].generateDot()

            return dot

    def toDot(self, filename):
        with open(filename, "w+") as f:
            f.write("graph G {\n")
            f.write(self.generateDot())
            f.write("\n}")
