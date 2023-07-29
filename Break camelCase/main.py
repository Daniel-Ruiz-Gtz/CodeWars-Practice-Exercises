"Break camelCase"
"""
Instructions
Output
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    result = ""
    for i in s:
        if i.isupper():
            result += " " + i
        else:
            result += i
    return result

print(solution("helloDanielRuizGtz"))

"Solution using a library"

import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)