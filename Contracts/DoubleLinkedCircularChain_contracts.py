from DoubleLinkNode import DoubleLinkNode


class DoubleLinkedCircularChain:
    def __init__(self):
        self.head = None
        self.count = 0

    def retrieve(self, index):
        """
        +retrieve(in index:integer): ListItemType, boolean
        Deze functie geeft de node van de gegeven index terug.
        :param index: Index van de node die je wilt vinden.
        :return: None als er niets is gevonden, anders de gevonden node. Daarnaast ook een succes boolean.
        Pre-condities: De parameter index moet van het type (positieve, kleiner dan self.count)integer zijn.
        Post-condities: Als er een corresponderende node gevonden is, zal deze teruggegeven worden.
        """
        pass

    def insert(self, index, newItem):
        """
        +insert(in index:integer, in newItem:ListItemType): boolean
        Insert een nieuw item op de plek "index" van de ketting.
        :param index: Plek waarop een nieuwe node moet toegevoegd worden.
        :param newItem: Waarde van de nieuwe node
        :return: succes Boolean
        Pre-condities: De parameter index moet van het type (positieve, kleiner dan self.count) integer zijn.
        Post-condities: Het object newItem zal op de plaats index ingevoegd worden.
        """
        pass

    def delete(self, index):
        """
        +delete(in index:integer): boolean
        Delete een node met gegeven index.
        :param index: De index van de te verwijderen node.
        :return: succes Boolean
        Pre-condities: De parameter index moet van het type (positieve, kleiner dan self.count) integer zijn.
        Post-condities: Als er op de plaats index een item zit, zal dit verwijdert worden.
        """
        pass

    def sort(self):
        """
        +sort(): boolean
        Sorteert de ketting van klein naar groot (op basis van ID)
        Pre-condities: geen.
        Post-condities: Als de lijst niet leeg is zal ze gesorteerd worden op de key van het object.
        """
        pass

    def isEmpty(self):
        """
        +isEmpty(): boolean
        :return: True als de lijst leeg is, anders False.
        Pre-condities: geen.
        Post-condities: Je krijgt een boolean(True/False) die aanwijst of de lijst leeg is of niet.
        """
        pass

    def getLength(self):
        """
        +getLength(): integer
        :return:
        Pre-condities: geen.
        Post-condities: Je krijgt de lengte van de lijst (0 als de lijst leeg is).
        """
        pass

    def traverse(self):
        """
        +traverse()
        Doorloopt de ketting.
        """
        pass

    def print(self):
        """
        +print()
        Geeft .dot code voor de structuur van de tree.
        """
