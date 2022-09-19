#September 12, 2022
#This program takes a user's input first and last names, as well as a hypothetical university email then prints as string.

firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
username = input("What is your email username? ")

print(firstName + " " + lastName)
print(lastName.upper() + ", " + firstName)
print(username)
print(username.lower() + "@hunter.cuny.edu")