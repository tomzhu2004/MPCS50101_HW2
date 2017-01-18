# @Date:   2017-01-15T22:16:05-06:00
# @Last modified time: 2017-01-15T23:44:37-06:00
#Prompt user for grade on a scale from 0-100.
score = int(raw_input("On a scale from 0-100, what grade did you get on the test?"))
#If user entered something other than 0-100, bug them to reenter.
if score < 0 or score > 100:
    print ("Wrong answer! Try again!")
if 90 <= score <= 100:
    print("You got an A. Congratulations!")
elif 80 <= score <90:
    print("You got a B. Not bad.")
elif 70 <= score <80:
    print("You got a C. Try harder next time.")
elif 60 <= score <70:
    print ("You got a D. Now you're just not trying.")
elif 0 <= score <60:
    print ("you got an F. Guess you're not getting that degree.")
