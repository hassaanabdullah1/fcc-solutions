'''                         'Acronym Builder'
Given a string containing one or more words,
return an acronym of the words using the following constraints:
 The acronym should consist of the first letter of each word capitalized, 
    unless otherwise noted.
 The acronym should ignore the first letter of these words unless they are
   the first word of the given string: a, for, an, and, by, and of.
 The acronym letters should be returned in order they are given.
 The acronym should not contain any spaces.'''
def build_acronym(s):
    ignore = ['a', 'for', 'an', 'and', 'by', 'of']
    acronym = ""
    s_list = [x.lower().strip() for x in s.split()]
    for indx, word in enumerate(s_list, start=1):
        if word in ignore and indx != 1:
            continue
        acronym += word[0].upper()

    return acronym


print(build_acronym("and a an for this"))
print(build_acronym("Search Engine Optimization"))
print(build_acronym("Frequently Asked Questions"))
print(build_acronym("National Aeronautics and Space Administration"))
print(build_acronym("Federal Bureau of Investigation"))
print(build_acronym("For your information"))
print(build_acronym("By the way"))
print(build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily"))
