"Extract the domain name from a URL"
"""
Instructions
Output
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def domain_name(url):
    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]

    if url.startswith("www."):
        url = url[len("www."):]

    dot_index = url.find(".")

    domain_name = url[:dot_index]
    return domain_name


print(domain_name("http://github.com/carbonfive/raygun"))

"""
I didn't know that i can import libraries, in this solution using regex
Other solution: 
"""

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name') 