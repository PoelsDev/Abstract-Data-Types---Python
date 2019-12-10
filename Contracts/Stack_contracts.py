from Node import Node


class Stack:
    def __init__(self):
        self.listHead = None

    def isEmpty(self):
        """
        +isEmpty(): boolean
        Deze functie checkt of de Stack leeg is of niet.
        :return: True of False
        Pre-condities: geen
        Post-condities: Geeft weer of de stack leeg is of niet.
        """
        pass

    def push(self, newItem):
        """
        +push(in newItem:StackItemType): boolean
        Voegt een item toe bovenop de stack.
        :param newItem: Nieuw toe te voegen item.
        :return: True of False: succes Boolean
        Pre-condities: De parameter newItem moet een object zijn met de getKey()-method.
        Post-condities:
        """
        pass

    def pop(self):
        """
        +pop(): stackItemType, boolean
        Haalt het laatste item vanop de stack eraf en geeft die weer.
        :return: Het gepopte item (None als de stack leeg is) en een succes Boolean.
        Pre-condities: geen
        Post-condities: Het bovenste item van de stack is er af gehaald en wordt teruggegeven.
        """
        pass

    def getTop(self):
        """
        +getTop(): stackItemType, boolean
        Geeft het bovenste item van de stack.
        :return: Returnt het item (None als de stack leeg is) en een succes Boolean
        Pre-condities: geen
        Post-condities: Als de stack niet leeg is zal het bovenste item teruggegeven worden.
        """
        pass
