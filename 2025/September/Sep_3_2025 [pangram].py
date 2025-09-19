import time
start_time = time.perf_counter()
'''
---Pangram---
Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.
    Ignore non-alphabetical characters in the word or sentence.
    Ignore letter casing in the word or sentence.
'''
def is_pangram(sentence, letters):
    new_sent = []
    #You can separate the characters in a string in Python by using the list() function, which converts the string into a list of its individual characters. For example, list("hello") will give you ['h', 'e', 'l', 'l', 'o']
    #dict.fromkeys() method creates a dictionary with keys from the list, automatically removing duplicates because dictionary keys are unique. The order is preserved where dictionaries maintain insertion order.
    found = False
    sentence = list(dict.fromkeys(sentence))
    new_let = list(x.lower() for x in letters) #could be simplified to [x.lower() for x in letters] or even done earlier when processing the input.
    for x in sentence:
        if not x == " " and x.isalpha(): #only checking of x.isalpha() would be snough here
                new_sent.append(x.lower())
            
    if set(new_let) == set(new_sent):
            found = True

    print(found)

is_pangram("hello", "helo") #should return True
is_pangram("hello", "hel") #should return False
is_pangram("hello", "helow") #should return False
is_pangram("hello world", "helowrd") #should return True
is_pangram("Hello World!", "helowrd") #should return True
is_pangram("Hello World!", "heliowrd") #should return False
is_pangram("freeCodeCamp", "frcdmp") #should return False
is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") #should return True

