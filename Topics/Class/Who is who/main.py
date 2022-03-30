class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"

    def __str__(self):
        return "{}\n{}\n{}".format(self.color, self.feature, self.home)



class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"

    def __str__(self):
        return "{}\n{}\n{}".format(self.color, self.feature, self.home)

angel = Angel()
demon = Demon()

print(angel)
print(demon)
