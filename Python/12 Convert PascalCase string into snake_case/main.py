"Convert PascalCase string into snake_case"
"""
Instructions
Output
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. 
If the method gets a number as input, it should return a string.
Examples:
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
"""
def to_underscore(string):
    sol = ""
    first = True
    for x in str(string):
        if x.isupper():
            if first == False:
                sol += "_"
            sol += x.lower()
            first = False
        else:
            sol += x.lower()
    return sol
            
print(to_underscore("TestController"))

"Another quick solution, not the best but short :)"
def to_underscore(string):
    return ''.join('_'+c.lower() if c.isupper() else c for c in str(string)).lstrip('_')