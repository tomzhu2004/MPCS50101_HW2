# @Date:   2017-01-16T01:20:38-06:00
# @Last modified time: 2017-01-18T02:18:35-06:00



#Program to find the gcd. Going to have to use loops now.
print "Welcome. This trifling program computes the greatest commond divisor for two numbers."
print "You will be prompted to assign values for both a and b."
value_a = int(input("Now please enter a value for a."))
try:
    print "You entered " + str(value_a) + " as the value for a."
except ValueError:
    print "This is not a integer. Please try again."
    value_a = int(input("Now please enter a value for a."))
    print "You entered " + str(value_a) + " as the value for a."
value_b = int(input("Now please enter a value for b."))
try:
    print "You entered " + str(value_b) + " as the value for b."
except ValueError:
    print "This is not a integer. Please try again."
    value_b = int(input("Now please enter a value for b."))
    print "You entered " + str(value_b) + " as the value for b."

raw_input("Now checking to see if a GCD exists. Pres any key to continue...")
#Create function for calculating gcd via subtraction
def gcd(value_a,value_b):

    while value_a != value_b:
        if value_a > value_b:
            value_a -= value_b
        elif value_b > value_a:
            value_b -= value_a
    return value_a

print (gcd(value_a,value_b))
