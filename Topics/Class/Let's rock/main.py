# start a RockBand here
class RockBand:
    genre = "rock"
    key_instruments = ["electric guitar", "drums"]
    n_members = 4

    def __str__(self):
        return "{}\n{}\n{}".format(self.genre, self.n_members, self.key_instruments)

my_band = RockBand()
print(my_band)
