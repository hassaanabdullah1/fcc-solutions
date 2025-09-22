'''
                    Digits vs Letters
Given a string, return "digits" if the string has more digits than letters,
"letters" if it has more letters than digits, and "tie" if it has the same
amount of digits and letters.
    Digits consist of 0-9.
    Letters consist of a-z in upper or lower case.
    Ignore any other characters
'''


def digits_or_letters(s):
    digits = []
    letter = []
    for char in s:
        if char.isdigit():
            digits.append(char)
        elif char.isalpha():
            letter.append(char.lower())

    if len(digits) > len(letter):
        return "digits"
    elif len(digits) < len(letter):
        return "letters"
    else:
        return "tie"

print(digits_or_letters("abc123")) #should return "tie"
print(digits_or_letters("a1b2c3d")) #should return "letters"
print(digits_or_letters("1a2b3c4")) #should return "digits"
print(digits_or_letters("abc123!@#DEF")) #should return "letters"
print(digits_or_letters("H3110 W0R1D")) #should return "digits"
print(digits_or_letters("P455W0RD")) #should return "tie"