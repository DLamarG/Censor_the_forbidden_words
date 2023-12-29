def censor_this(text, forbidden_words):
    cen_str = []
    words_of_phrase = text.split(' ')
    for wrd in words_of_phrase:
        if wrd.lower() not in forbidden_words:
            cen_str.append(wrd)
        if wrd.lower() in forbidden_words:
            new_str = '*'*len(wrd)
            cen_str.append(new_str)
    return ' '.join(cen_str)




print(censor_this("The cat does not like the fire", ["cat", "fire"]))
print(censor_this("The cat does not like the therapy", ["the", "like"]))
print(censor_this("Javascript is the BEST programming language and LOLCODE is the Worst", ["worst", "best"]))
print(censor_this("A bald eagle is a worthy adversary", ["bald", "a"]))