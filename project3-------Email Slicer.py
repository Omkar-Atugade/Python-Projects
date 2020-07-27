#Taking email as a input form user

email = input("Enter your Email address: ").strip()

#Slicing user name from email

user_name = email[:email.index('@')]

#Slicing domain name from email

domain_name = email[email.index('@')+1: ]

#Formating message we have

output = "Your user name is {} and domain name is {}.".format(user_name, domain_name)

#Displaying output message

print(output)


