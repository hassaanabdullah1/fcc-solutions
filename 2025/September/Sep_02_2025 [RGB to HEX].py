'''
                        RGB to Hex
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.
Here are some example outputs for a given input:
       Input                 Output
"rgb(255, 255, 255)" 	   "#ffffff"
"rgb(1, 2, 3)" 	           "#010203"
    Make any letters lowercase.
    Return a # followed by six characters. Don't use any shorthand values.


'''

hex_key = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}

def rgb_to_hex(rgb):
    num_str = rgb[4:-1]
    values = [int(x) for x in num_str.split(",") ]
    rgb = []
    for value in values:
        digit_1 = value // 16
        digit_2 = value % 16
        rgb.append(str(hex_key[digit_1]) + str(hex_key[digit_2]))
    rgb = "#"+"".join(rgb)

    return rgb


print(rgb_to_hex("rgb(255, 255, 255)")) #should return "#ffffff"
print(rgb_to_hex("rgb(1, 11, 111)")) #should return "#010b6f"
print(rgb_to_hex("rgb(173, 216, 230)")) #should return "#add8e6"
print(rgb_to_hex("rgb(79, 123, 201)")) #should return "#4f7bc9
