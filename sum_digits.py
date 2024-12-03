num=int(input("enter a number :"))
total=0
while num>0:
    total+=num%10
    print(f"now total is: {total}")
    num//=10
    print(f"remaining digits are: {num}")
print(f"sum of given number: is {total}")
