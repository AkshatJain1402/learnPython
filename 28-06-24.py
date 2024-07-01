# couting vowels a,e,i,o,u
s="hey how are you doing"


def checkVowels(text):
    count=0
    for i in text:
        if i=="a" or i =="o" or i =="u" or i== "e"  or i=="i" or i=="I" or i=="A" or i=="O" or i=="U":
            count +=1
    return count 

print(checkVowels(s))


#Method 2 using count 
result=s.count("a")+s.count("e")+s.count("o")+s.count("i")+s.count("u")
print(result)


#Method 3 using IN operator



def checkVowels(text):
    count=0
    vowels="aeiouAEIOU"
    
    print(count)
    for i in text:
        
        if i in vowels:
            count +=1
    return count

print(checkVowels(s))

#Method 4 creating a dict
def checkVowels(text):
    vowels="aeiouAEIOU"
    count={v:0 for v in vowels}
    
    print(count)
    for i in text:    
        if i in vowels:
            count[i]=+1   
    return count

print ("Method 4 dictionary",checkVowels(s))

