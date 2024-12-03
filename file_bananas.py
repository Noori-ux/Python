textFile=open("poem.txt","w+")
my_poem='''abcdefg orange
bananas apples grapes watermelons
grapefruits'''
textFile.write(my_poem)
textFile.close()
newFile=open("poem.txt")
#print(newFile.read())

myString=newFile.read()
print(type(myString))
print(myString)
myString=myString.replace("grapes","blueberries")
print(myString)
newFile.close()
newFile=open("poem.txt","w+")
newFile.write(myString)
newFile.close()
