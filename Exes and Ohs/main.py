"Exes and Ohs"
"""
Instructions
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
"My solution (It is a very bad solution and not eficient at all"
def xo(s):
    x = 0
    o = 0
    for i in range(len(s)):
        if s[i] == 'x' or s[i] == 'X':
            x += 1
        if s[i] == 'o' or s[i] == 'O':
            o += 1
    if x == o:
        return True
    else:
        return False 

print(xo("zpzpzpp"))

"Another much better implemented solution"
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo("zpzpzpp"))