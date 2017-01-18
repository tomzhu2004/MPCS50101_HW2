# @Date:   2017-01-15T23:44:57-06:00
# @Last modified time: 2017-01-18T02:19:02-06:00



print "Welcome! This program checks to see if a is a power of b."
#first time using int command to test whether integer or not
value_a = (raw_input("Now please enter a value for a."))

try:
    int(value_a)
    print "You entered " + str(value_a) + " as the value for a."
except ValueError:
    print "This is not a integer. Please try again."
    value_a = (raw_input("Now please enter a value for a."))
    print "You entered " + str(value_a) + " as the value for a."

value_b = (raw_input("Now please enter a value for b."))

try:
    int(value_b)
    print "You entered " + str(value_b) + " as the value for b."
except ValueError:
    print "This is not a integer. Please try again."
    value_b = (raw_input("Now please enter a value for b."))
    print "You entered " + str(value_b) + " as the value for b."
#I could have done a loop, but too lazy right now and not too sure how to. TBC
a_over_b = float(value_a) / float(value_b)
ab_over_b = float(a_over_b) / float(value_b)
if float(value_a)%float(value_b) == 0 and float(ab_over_b)%float(value_b) == 0:
    print "True."
else:
    print "False."
