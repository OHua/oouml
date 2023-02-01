class Duck:
    def __init__(self, name):
        self.name = name

    def quack(self):
        print("c c c")

    def fly(self):
        print("i can fly")


class GreenHeadDuck(Duck):
    def __init__(self, name):
        super().__init__(name)
        self.color = "green"


class WoodDuck(Duck):
    def quack(self):
        print("i can't quack")

    def fly(self):
        print("i can't fly")


class YellowPlasticDuck(Duck):
    def quack(self):
        print("ji ji ji")

    def fly(self):
        print("i can't fly")