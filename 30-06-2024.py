# # Capitalize First Letter of Each Word:


# text="hy my name is akshat jain and currenty living in India"
# #method 1 using built in  method title()
# print(text.title())

# #method2 using different approach
# words=[]
# words=text.split(" ")
# text=""
# for index,word in enumerate(words):
#     lst=list(word)
#     lst[0]=str(lst[0]).upper()
#     lst+=" "
    
#     words[index]="".join(lst)
#     text+="".join(lst)

# print(text)


### Remove duplicates
#Method1 

Original="Mississippi"
# Without duplicates: MISP
output=[]
for i in Original:
    if not output.count(i)>0 :
        
        output.append(i)


print(Original+"l")