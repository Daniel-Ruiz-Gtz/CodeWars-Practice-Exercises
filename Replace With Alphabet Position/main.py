"Replace With Alphabet Position"
"""
Instructions
Output
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

"""

def alphabet_position(text):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            result.append(str(ord(char) - ord('A') + 1))
        elif 'a' <= char <= 'z':
            result.append(str(ord(char) - ord('a') + 1))
    return ' '.join(result)

print(alphabet_position("Hello Daniel"))

"Short Solution:"
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

"""
To get this kata I have to investigate about convert the character in a number and the use logic to follow the instructions
    
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