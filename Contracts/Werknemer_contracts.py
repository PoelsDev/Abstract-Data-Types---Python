class Werknemer:
    def __init__(self, id, voornaam, achternaam, workload):
        self.id = id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.workload = workload
        self.currentBestelling = None

    def add_CurrentBestelling(self, bestelling):
        """
        +add_CurrentBestelling(in bestelling:Bestelling)
        Als de werknemer met een bestelling bezig is refereert deze functie naar deze bestelling (zodat beide tijdelijk gelinkt zijn)
        :param bestelling: De bestelling waarmee de werknemer bezig is.
        Pre-condities: De parameter moet een instantie zijn van de klasse Bestelling
        Post-condities: De attribuut currentBestelling van de werknemer zal ingevuld worden.
        """
        pass

    def __str__(self):
        return f'Werknemer | ID: {self.id}, Naam: {self.voornaam} {self.achternaam}, Workload: {self.workload}.'

    def getKey(self):
        """
        +getKey(out workload: integer)
        Deze functie geeft van het object de workload attribuut terug.
        :return: self.workload
        Pre-condities: geen
        Post-condities: de attribuut "timestamp" zal teruggegeven worden.
        """
        pass
