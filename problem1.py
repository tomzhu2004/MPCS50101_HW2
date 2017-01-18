# @Date:   2017-01-15T21:39:36-06:00
# @Last modified time: 2017-01-15T23:44:30-06:00
#Prompt user for temperature in Fahrenheit and convert into Celsius.
temp_f = int(raw_input("What temperature would you like to convert to Celsius?"))
#Use str function to allow combination of text and numbers.
temp_c = str(temp_f - 32 * 5/9)
print "That is " + temp_c + " degrees Celsius."
