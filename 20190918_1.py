class intigerNum:
    'valamit'
    def __init__(self,p1):
        self.number = p1
    def doubleNum(self):
        return self.number*2
    def squareNum(self):
        return self.number**2
    def pow(self,k):
        return self.number

p1=intigerNum(5)
p2=intigerNum(5)
p3=p1

print(p1.number)
print(p1.doubleNum())

print(p1==p3)