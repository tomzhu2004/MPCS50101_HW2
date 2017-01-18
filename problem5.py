# @Date:   2017-01-17T21:57:19-06:00
# @Last modified time: 2017-01-18T13:07:06-06:00



#This program is a password validator.
print "Welcome! Please create a password that you will use for your account."
raw_input("Please press any key to continue...")
#Just a little something extra. Helps break up the flow.
print "To create a strong password you will need to meet the following criteria."
print "1. It must have at least 12 characters."
print "2. It must contain both numbers and letters."
print "3. It must contain at least one of the following !@#$%"
print "4. It must contain at least one capital letter and one lower case letter."
raw_input("Is that clear? If so press any key to continue...")
password = raw_input("Please create a password now.")
print "You entered " + password + "."

#Checks to see if password meets the above criteria. I'm sure a better way could be written, but too stupid/lazy at this point.

if len(password) <= 12:
    print "Password does not meet length requirements. Please try again."
    #Checks to see if password is at least 12 characters.
elif password.isdigit() == True:
    print "Password requires both numbers and letters. Please try again."
    #Checks to see if password is all numbers. Rejects if this is true.
elif password.isupper() == True:
    #Checks to see if password has only capital letters. Rejects if this is true.
    print "Password requires both upper case and lower case letters. Please try again."
elif password.islower() == True:
    #Checks to see if all lower case.
    print "Password requires both upper case and lower case letters. Please try again."
elif "!" not in password == True or "@" not in password == True or "#" not in password == True or "$" not in password == True or "%" not in password == True:
    print "Password requires at least one of the following !@#$%"
else:
    print "Password accepted. Thank you."
