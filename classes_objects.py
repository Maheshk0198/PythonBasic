class addition:
    def __init__(self, a , b):
        self.a = a
        self.b = b
    def myadd(self, c):
        print(self.a+self.b+c)

num = int(input())
mynum = addition(4,8)
mynum.myadd(num)