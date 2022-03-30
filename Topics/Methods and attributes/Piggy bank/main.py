class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents


    def add_money(self, dollars, cents):
        self.dollars += dollars
        self.cents += cents

        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents %= 100
