str1 = "hello world"
str2 = ""
#HloWrd
for i in range(len(str1)):
   # print(i)
    if i%2==0:
        str2+=str1[i]
        print(f"position: {i} and the character is: {str1[i]}")
        
print(str2)
