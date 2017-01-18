# @Date:   2017-01-18T02:15:24-06:00
# @Last modified time: 2017-01-18T12:21:23-06:00

print "Welcome. This fun little program builds an asterisk pyramid."
raw_input("Press any key to continue...")
number = int(input("Please enter the desired height of your pyramid."))

def triangle(height):
    #max number of asterisks per row is equal to row height
    no_asterisks = height
    spaces = int(height-1)
    #spaces - if 5 asterisks then you want 4 spaces, etc.
    for i in range (0, height):
        print (" " * spaces + "*" * (1+i))
        spaces = spaces - 1
triangle(number)
