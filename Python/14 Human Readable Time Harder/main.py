"Human Readable Time Harder"
"""
Instructions
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
It is much easier to understand with an example:
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.
Note that spaces are important.
"""
def format_duration(seconds):
    if seconds == 0:
        return "now"
    y, seconds = divmod(seconds, 365 * 24 * 3600)
    d, seconds = divmod(seconds, 24 * 3600)
    h, seconds = divmod(seconds, 3600)
    m, seconds = divmod(seconds, 60)
    components = []
    
    if y:
        components.append(f"{y} year{'s' if y > 1 else ''}")
    if d:
        components.append(f"{d} day{'s' if d > 1 else ''}")
    if h:
        components.append(f"{h} hour{'s' if h > 1 else ''}")
    if m:
        components.append(f"{m} minute{'s' if m > 1 else ''}")
    if seconds:
        components.append(f"{seconds} second{'s' if seconds > 1 else ''}")
        
    if len(components) == 1:
        return components[0]
    
    if len(components) == 2:
        return " and ".join(components)
    
    return ", ".join(components[:-1]) + " and " + components[-1]


print(format_duration(3600))
print(format_duration(253374061))
print(format_duration(0))