"Rot13"
"""
Instructions
Output
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.
"""
def rot13(message):
    result = ""
    for char in message:
        if char.isalpha():
            is_uppercase = char.isupper()
            char_code = ord(char.lower()) - ord('a')
            shifted_code = (char_code + 13) % 26
            new_char = chr(shifted_code + ord('a'))
            if is_uppercase:
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result

print(rot13("aA bB zZ 1234 *!?%"))

"""
Took this table from Replace With Alphabetic Position Kata
    
A  ->  65  |  a  ->  97
B  ->  66  |  b  ->  98
C  ->  67  |  c  ->  99
D  ->  68  |  d  ->  100
E  ->  69  |  e  ->  101
F  ->  70  |  f  ->  102
G  ->  71  |  g  ->  103
H  ->  72  |  h  ->  104
I  ->  73  |  i  ->  105
J  ->  74  |  j  ->  106
K  ->  75  |  k  ->  107
L  ->  76  |  l  ->  108
M  ->  77  |  m  ->  109
N  ->  78  |  n  ->  110
O  ->  79  |  o  ->  111
P  ->  80  |  p  ->  112
Q  ->  81  |  q  ->  113
R  ->  82  |  r  ->  114
S  ->  83  |  s  ->  115
T  ->  84  |  t  ->  116
U  ->  85  |  u  ->  117
V  ->  86  |  v  ->  118
W  ->  87  |  w  ->  119
X  ->  88  |  x  ->  120
Y  ->  89  |  y  ->  121
Z  ->  90  |  z  ->  122
"""