#!/usr/bin/python3
"""This project is to mimic the emial slicer where an email is being reduced
to names and domain.
1. it asks the user for their names
 2.use strip to remove spaces at the begining and end
 3. use rindex tpo get the location of  a given character
 finally it  uses string slicing to slice of the given character"""

while True:
    user_email =str(input("Please put your valid email: ")).strip()
    index1 = user_email.split('@')
    name = index1[0]
    domain = index1[-1]
    if "@" not in user_email or ' ' in name or '.' not in domain or " " in domain:
        print('please put in a valid email address')
    else:
        print("Your Name: {0}\nYour Doamin: {1}".format(name, domain))
        break
