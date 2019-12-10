class TimeDelta:
    def __init__(self):
        self.time = 0

    def TimeUp(self):
        """
        Voegt een tijdseenheid toe bij de tijd.
        """
        self.time += 1
