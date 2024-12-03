num=int(input("enter a number between 1 to 100. "))

def printBuzz(num):
    if num%5 == 0:
        print("Buzz")


def printFizz(num):
        if num%3 == 0:
            print("Fizz")


def printFizzBuzz(num):
        if (num%5 == 0 and num%3 == 0):
                print("FizzBuzz")


printBuzz(num)
printFizz(num)
printFizzBuzz(num)

