##text=open("story.txt")
###file=text.read()
##line_no=1
##for line in text:
##    print(f"line number is {line_no} and {line}")
##   # print("\n")
##    line_no+=1
###print(file)
##text.close()

text_w=open("story.txt","w+")
text_w.write("oranges")
print(text_w.read())
text_w.close()


