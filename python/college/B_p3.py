import random
class MyException(Exception):
    num=random.randint(1,150)
    def getNum(self):
        n=int(input("Guess a number between 1 to 150: "))
        if n>self.num:
            raise MyException("Entered number is greater than computer's guess.")
        elif n<self.num:
            raise MyException("Entered number is less than computer's guess.")
        else:
            print("You have guessed correct!!")
            return 1
e=MyException()
for i in range(1,10):
    try:
        r=e.getNum()
        print()
        if r==1:
            break
    except MyException as me:
        print(me)
if i==9:
    print("You have failed to guess....")