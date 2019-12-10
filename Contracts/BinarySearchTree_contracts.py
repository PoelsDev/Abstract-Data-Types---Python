from TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.parent = None
        self.leftTree = None
        self.rightTree = None

    def searchTreeInsert(self, newItem):
        """
        +searchTreeInsert(in NewItem: TreeItemType): boolean
        Deze functie insert een newItem in de binaire boom.
        :param newItem: NewItem dat moet worden toegevoegd.
        :return: True of False (success Boolean)
        Pre-condities: De parameter newItem moet een object met de getKey()-functie bevatten.
        Post-condities: Het object zal aan de binaire zoekboom worden toegevoegd. (Tenzij dezelfde key als een ander object)
        """
        pass

    def searchTreeRetrieve(self, searchKey):
        """
        +searchTreeRetrieve(in searchKey: KeyType,out treeItem: TreeItemType)
        Deze functie zoekt een bepaalde key in de binaire zoekboom op basis van een gegeven searchKey en geeft het daarbij horende object terug.
        :param searchKey: Te zoeken key
        :return: None als er geen gevonden is, een object (treeItem) als er wel 1 gevonden is.
        Pre-condities: De parameter searchKey moet een object met de getKey()-functie bevatten.
        Post-condities: Er zal een object zijn teruggegeven met de overeenkomstige sleutel.
        """
        pass

    def searchTreeRetrieveSubTree(self, searchKey):
        """
        ** ENKEL VOOR INTERN GEBRUIK **

        +searchTreeRetrieveSubTree(in searchKey: KeyType, out: BST)
        Deze functie is analoog aan de searchTreeRetrieve()-functie. Alleen returnt deze functie een SubTree i.p.v. een object.
        :param searchKey: De key waarvan de SubTree moet gezocht worden.
        :return: None als er geen gevonden is, een SubTree als de key gevonden is.
        Pre-condities: De parameter searchKey moet een getKey()-functie hebben om te werken.
        Post-condities: De functie geeft een subtree terug waarvan het object in de root de overkomstige key heeft.
        """
        pass

    def searchTreeDelete(self, searchKey):
        """
        +searchTreeDelete(in searchKey: KeyType): boolean
        Deze functie delete met een gegeven key, een object uit de boom.
        :param searchKey: De key waarvoor een te verwijderen object moet gevonden worden.
        :return: False als het mislukt is, True als het gelukt is.
        Pre-condities: De parameter searchKey moet een getKey() functie hebben om te werken.
        Post-condities: Het object met de overeenkomstige sleutel zal verwijdert zijn.
        """
        pass

    def deleteWithRightTree(self, deleteItem):
        """
        ** ENKEL VOOR INTERN GEBRUIK **

        +deleteWithRightTree(in deleteItem: TreeItemType)
        Deze functie wordt gebruikt in de searchTreeDelete()-functie in het geval dat het te verwijderen object enkel een rechter deelboom heeft.
        Het zal voor deze omstandigheid een specifieke verwijdering uitvoeren.
        :param deleteItem: Het te verwijderen item.
        Pre-condities & post-condities n.v.t. wegens intern gebruik.
        """
        pass

    def deleteWithBothChildren(self, deleteItem):
        """
        ** ENKEL VOOR INTERN GEBRUIK **

        +deleteWithBothChildren(in deleteItem: TreeItemType)
        Deze functie wordt gebruikt in de searchTreeDelete()-functie in het geval dat het te verwijderen object twee deelbomen heeft.
        Het zal voor deze omstandigheid (m.b.v. de searchTreeLeftSuccessor()-functie) een specifieke verwijdering uitvoeren.
        :param deleteItem: Het te verwijderen object.
        Pre-condities & post-condities n.v.t. wegens intern gebruik.
        """
        pass

    def deleteWithLeftTree(self, deleteItem):
        """
        ** ENKEL VOOR INTERN GEBRUIK **

        +deleteWithLeftTree(in deleteItem: TreeItemType)
        Deze functie wordt gebruikt in de searchTreeDelete()-functie in het geval dat het te verwijderen object enkel een linker deelboom heeft.
        Het zal voor deze omstandigheid een specifieke verwijdering uitvoeren.
        :param deleteItem: Het te verwijderen item.
        Pre-condities & post-condities n.v.t. wegens intern gebruik.
        """
        pass

    def searchTreeLeftSuccessor(self):
        """
        ** ENKEL VOOR INTERN GEBRUIK **

        +searchTreeLeftSuccessor(): BST
        Zoekt de inorder successor(-subTree) nadat er al 1 maal naar rechts gegaan is.
        :return: Boom waarin de successor zich in de root bevindt.
        Pre-condities & post-condities n.v.t. wegens intern gebruik.
        """
        pass

    def isEmpty(self):
        """
        +isEmpty(): boolean
        Deze functie checkt of de binaire boom leeg is of niet.
        :return: True als de boom leeg is, anders False.
        Pre-condities: geen.
        Post-condities: Geeft een boolean terug die weergeeft of de BST leeg is of niet.
        """
        pass

    def getRootData(self):
        """
        +getRootData(): TreeItemType, boolean
        Deze functie returnt het object van de root van de binaire boom waarin het wordt aangeroepen.
        :return: None als de boom leeg is, de rootdata als de boom niet leeg is. Daarnaast ook nog een succes boolean.
        Pre-condities: geen.
        Post-condities: Als de BST niet leeg is zal de data van het item in de root weergegeven worden (__str__-method)
        """
        pass

    def setRootData(self, newItem):
        """
        +setRootData(in newItem: TreeItemType): boolean
        Dit is dezelfde als de getRootData()-functie, alleen verandert dit de rootdata. Creëert een nieuwe node met daarin newItem als de boom
        leeg is.
        :param newItem: Nieuwe rootobject
        :return: een succes Boolean
        Pre-condities: De parameter newItem moet een getKey()-functie hebben.
        Post-condities: De inhoud van de root waarvan deze functie is aangeroepen zal veranderd zijn.
        """
        pass

    def getLeftSubtree(self):
        """
        +getLeftSubtree(): BST
        Geeft de linkse subTree.
        :return: Een lege binaire boom als de boom leeg is, anders de linkse Subtree.
        Pre-condities: geen.
        Post-condities: Als de BST niet leeg is zal de leftTree gereturnd worden. Anders zal er een lege boom teruggegeven worden.
        """
        pass

    def getRightSubtree(self):
        """
        +getRightSubtree(): BST
        Geeft de rechtse subTree.
        :return: Een lege binaire boom als de boom leeg is, anders de rechtse Subtree.
        Pre-condities: geen.
        Post-condities: Als de BST niet leeg is zal de rightTree gereturnd worden. Anders zal er een lege boom teruggegeven worden.
        """
        pass

    def inorderTraverse(self):
        """
        +inorderTraverse()
        Doorloopt de boom in inorder traverse en print de __str__ method van de objecten af (TreeItemType).
        Pre-condities: geen.
        Post-condities: De boom zal (als niet leeg) in inorder traverse doorlopen worden.
        """
        pass

    def __str__(self):
        lines = printTree(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    def generateDot(self):
        # dot = ""
        # link = "--"
        # newline = \n
        # dot+=newline
        # dot+=str(self.root)
        # Basisgeval
        # if self.leftTree is None:
        #   dot+="link + ""a" + str(random.randint(1,100)
        # else:
        #   dot+=str(self.leftTree.root)
        #
        # dot += newline
        # dot+=str(self.root)+link
        # if self.leftTree is None:
        #   dot+="link + ""a" + str(random.randint(1,100)
        # else:
        #   dot+=str(self.leftTree.root)

        # recursieve stap
        # if self.leftTree is not None:
        #   dot += self.leftTree.generateDot()
        # if self.leftTree is None:
        #     dot += self.rightTree.generateDot()
        # return dot
        pass

    def toDot(self):
        pass

    def printsearchTree(self):
        """
        +printsearchTree()
        //Geeft .dot code voor de structuur van de tree.
        """
        pass



def printTree(tree, curr_index, index=False, delimiter='-'):
    if tree is None or tree.isEmpty():
        return [], 0, 0, 0

    line1 = []
    line2 = []
    node_repr = str(tree.root.key.getKey())

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = \
        printTree(tree.leftTree, 2 * curr_index + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        printTree(tree.rightTree, 2 * curr_index + 2, index, delimiter)

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end
