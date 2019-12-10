from TwoThreeFourNode import TwoThreeFourNode


class TwoThreeFourTree:
    def __init__(self):
        self.root = None
        self.parent = None
        self.subtrees = [None]*3

    def inorder(self):
        """
        +inorder(in tree:TwoThreeTree)
        Doorloopt de niet-lege 2-3-4 tree in volgorde van de keys.
        Pre-condities: geen.
        Post-condities: De boom wordt doorlopen in volgorde van de keys.
        """
        pass

    def retrieveItem(self, searchKey):
        """
        +retrieveItem(in searchKey:KeyType, out:TreeItemType):boolean
        Als het item met de key (searchKey) zich bevindt in de boom zal dit item teruggegeven worden.
        :param searchKey: Zoeksleutel waarvoor een corresponderend item moet worden gevonden.
        :return: True of False op basis van het succes van de functie en het gevonden item (bij True)
        Pre-condities: De parameter searchKey moet een getKey()-functie ter beschikking hebben.
        Post-condities: Een item wordt teruggegeven uit de 2-3-4 tree.
        """
        pass

    def insertItem(self, newItem):
        """
        +insertItem(in newItem:TreeItemType)
        Voegt een item toe aan de 2-3-4 tree.
        :param newItem: Het toe te voegen item.
        Pre-condities: De parameter newItem moet een getKey()-functie ter beschikking hebben.
        Post-condities: Het item zal in de boom zijn toegevoegd.
        """
        #TODO: Stap 1 - Maak insert


    def split(self, TreeNode):
        """
        +split(inout TreeNode: TreeNode)
        Splitst de node TreeNode op als het 3 items bevat.
        :param TreeNode: Node die gesplitst moet worden.
        :return: Gesplitste node
        Pre-condities: Een 2-3 tree node moet gegeven worden.
        Post-condities: De node zal als het te veel items bevatten gesplitst worden.
        """
        pass

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
        pass

    # def fix(self, TreeNode):
    #     """
    #     +fix(in TreeNode:TreeNode)
    #     Na verwijdering herverdeelt/voegt deze functie de items (samen).
    #     :param TreeNode: TreeNode die moet hervormd worden.
    #     Pre-condities: geen.
    #     Post-condities: De gegeven node zal nu hervormd zijn in de juiste vorm volgens de 2-3-4 tree.
    #     """
    #     pass

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
