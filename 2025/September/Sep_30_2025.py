'''Phone Number Formatter

Given a string of ten digits, return the string as a phone number in this 
format: "+D (DDD) DDD-DDDD" '''
def format_number(number):

    return f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:11]}"
print(format_number("05552340182")) #should return "+0 (555) 234-0182"
print(format_number("15554354792")) #should return "+1 (555) 435-4792"