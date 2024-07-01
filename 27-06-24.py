# #reverse a string 

# S="abcdefg"
# result=""

# #Method 1 using loops and range

# for i in range(len(S)-1,-1,2): 
#     result+=S[i]
#     print(i)
# #lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #lst[::2]
# #0+2=2+2=4+2=6+2=8
# # Extract every second element from index 1 to 8
# # print(lst[::-1]) 
# print(result)   
# #0-1=-1-1=-2-1=-3 ...... end tk 


# ###Method 2 ->slicing 


#         # The basic syntax for slicing is sequence[start:stop:step], where:

#         # start is the index where the slice starts (inclusive).
#         # stop is the index where the slice ends (exclusive).
#         # step is the interval between each index in the slice.

# print(S[::-1])


# #Method 3 -> builtin functions 

# lst=[]


# #pallindrome 

# pall="aabbaa"

# def isPallindrome(s):
#     return s==s[::-1]

# if isPallindrome(pall):
#     print("yes pallindrome")
# else:
#     print("not pallindrome")

#removing everything alpha numerics and special symbols

# pall=pall.replace("b","")

mixString="hey@#gunee&t"




for i in range(0,len(mixString)):
    
    print("index",i)
    #   hey#
    if 96 < ord(mixString[i] )< 123:
        print(mixString[i])
        
    else:
        mixString=mixString.replace(mixString[i],"")
    print("len",len(mixString))
    


       
    


