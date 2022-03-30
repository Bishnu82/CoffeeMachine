# our class Ship
class Ship:
    def __init__(self, name, country):
        self.name = name

        self.country = country

    # the old sail method that you need to rewrite
    def sail(self):
        return "The {} has sailed for {}!".format(self.name, self.country)


country_sail = input()
black_pearl = Ship("Black Pearl", country_sail)
print(black_pearl.sail())
