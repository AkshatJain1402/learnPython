# Capitalize First Letter of Each Word:


text="hy my name is akshat jain and currenty living in India"
#method 1 using built in  method title()
print(text.title())

#method2 using different approach
words=[]
words=text.split(" ")
text=""
for index,word in enumerate(words):
    lst=list(word)
    lst[0]=str(lst[0]).upper()
    lst+=" "
    
    words[index]="".join(lst)
    text+="".join(lst)

print(text)