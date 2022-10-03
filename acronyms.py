""" This project is to get user input phrase anf then get the acrome using the first alpabet of the wors after it is being splited """

user_input = str(input("Enter a Phrase: ")).split()
a = " "
for i in user_input:
    a = a + str(i[0]).upper() 
print(a)
