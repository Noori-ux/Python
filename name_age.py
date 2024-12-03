name=input("do you want to read a name or enter a name?: read/name: ")
age=input("enter age or read age?: read/enter: ")
if name == "read" and age == "read":
    name_age=open("name_age.txt")
    print(name_age.read())
else:
    name_age=open("name_age.txt","w+")
    dog= f"my dog's name is: {name} \n and my dog is {age} yrs \n"
   # dogAge= f"my dog is {age} yrs \n"
    name_age.write(dog)
    #name_age.write(dogAge)
name_age.close()
