class Queue:
    def __init__(self, size):
        self.front = None
        self.back = None
        self.items = [None] * size
        self.size = size

    def getFront(self):
        """
        +getFront(): queueItemType, boolean
        Geeft het eerste item van de queue terug + een boolean die succes aanduidt.
        Pre-condities: geen
        Post-condities: Geeft een tuple met daarin als eerste item de queueFront en als tweede
        item een boolean die aanduidt of de front gevonden is of niet.
        """
        pass

    def isEmpty(self):
        """
        +isEmpty(): boolean
        Deze functie checkt of de queue leeg is of niet.
        :return: True of False
        Pre-condities: geen
        Post-condities: Geeft met een boolean weer of de queue leeg is of niet.
        """
        pass

    def dequeue(self):
        """
        +dequeue(): boolean
        Verwijdert eerste item uit de queue.
        :return: True of False
        Pre-condities: geen
        Post-condities: De queueFront wordt verwijderd.
        """
        pass

    def enqueue(self, newItem):
        """
        +enqueue(in newItem:QueueItemType): boolean
        Voegt een item toe aan de queue (achteraan).
        :param newItem: Nieuw toe te voegen item.
        :return: True of False
        Pre-condities: geen
        Post-condities: De parameter newItem zal toegevoegd worden aan de queue.
        """
        pass
