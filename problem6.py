# @Date:   2017-01-18T02:58:27-06:00
# @Last modified time: 2017-01-18T03:33:41-06:00

#Program to test if a number is divisible by 11 without using modulus.
print "Welcome. This program checks to see if a given value is divisible by 11."
value = int(input("Please enter a number."))
#Now convert the number into a list.
value_list = map(int,list(str(value)))
#Now parse the list of integers into alternating, e.g 1,3,5,7 and 2,4,6,8
a = value_list[0::2]
b = value_list[1::2]
#Now subtract the sum of a by the sum of b. Let c = the abs of the difference.
c = abs(sum(a) - sum(b))
#If c equals 0 or 11 then it means the original number is divisible by 11.

if c == 0 or c == 11:
    print "Yes " + str(value) + " is divisible by 11."
else:
    print "No " + str(value) + " is not divisible by 11."
#End program.
