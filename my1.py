class Woman:

    def __init__(self,Weight,Height,IQ):
        self.Weight = Weight
        self.Height = Height
        self.IQ = IQ

    def eat(self):
        print(self.Weight + 10)

    def sleep(self):
        print(self.Height + 10)

    def study(self):
        print(self.IQ + 50)
