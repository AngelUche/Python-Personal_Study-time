#!/usr/bin/python3

"""This project is to mimic the emial slicer where an email is being reduced
to names and domain.
1. it asks the user for their names
 2.use strip to remove spaces at the begining and end
 3. use rindex tpo get the location of  a given character
 finally it  uses string slicing to slice of the given character"""

choice = 1
while True:
    user_email =str(input("Please put your valid email: ")).strip()
    if "@" not in user_email:
        print('please put in a valid email address')
    else:
        index1 = user_email.rindex('@')
        name = user_email[:index1].title()
        domain = user_email[index1 + 1:].title()
        print("Your Name: {0}\nYour Doamin: {1}".format(name, domain))
        break
