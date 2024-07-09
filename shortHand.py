text = "hy my name is akshat jain and currently living in india"
words = text.split(" ")

#short hand version of creating a list 
capitalized_words = [word[0].upper() + word[1:] for word in words]

#normal way of writing
capitalized_words = []
for word in words:
    capitalized_word = word[0].upper() + word[1:]
    capitalized_words.append(capitalized_word)