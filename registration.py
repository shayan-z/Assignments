# Welcome message to random people
print("Welkom to our platform with the most amazing users. My name is Mr lier and i am here to steal your data.")

# Asking the name of user
name = input("What is your name? ")

# Greating the user
print("Nice to have you here " + name.capitalize())

# Asking the lastname of user
lastname = input("What is your lastname? ").upper()

# Calculate lastname length
lastname_len = len(lastname)

# Change lastname_len to int
lastname_int = int(lastname_len)

# Check if we are family. Lastname should match Zarrinsadaf or ZARRINSADAF. 
if lastname == "ZARRINSADAF":
	print("Hey we are family, however you are the ugly one!")
else:
	print("OoooOoooOOooops, we are not family, however you can use my platform")

# Asking for user gender
user_gender = input("What is your gender?(male/female) ").upper()

# Asking user age
user_age = input("How old are you? ")
	
# Change user age to number
user_age_int = int(user_age)

# Calculate if user can acces our platform
user_age_minus = abs(user_age_int - 18)

# Check if the user is above 18 year if not exit
if user_age_int < 18:
	print("You are not old enough to use my platform. Come back in " + str(int(user_age_minus)) + " years")
	exit()
	
# Asking user if he/she wants advertisement
user_advertising = input("Would you like to get advertisement?(yes/no) ").upper()

# Check statement: Are we family or not and if the user would like to get advertisment
if user_advertising == "YES" and lastname != "ZARRINSADAF":
	# calculate how long lastname is and showing by that advertisment 
	count = 0
	while (count < lastname_int):
	   print('We are going to use your info to show you some advertisement!!!!')
	   count = count + 1	
	print("You get advertisement by how long your lastname is!!!")	
	print('Enjoy your stay')
	exit()
elif user_advertising == "YES" and lastname == "ZARRINSADAF":
	print("We don't use family data! Have fun using our platform!")
else:
	# Asking if user is single
	user_intrest = input("Are you single?(yes/no) ").upper()

# Calculate age and lastname and put it in user_value
user_value = lastname_int * user_age_int

# Change user value to int
user_value_int = int(user_value)

# Check statement: See if user is single + if user would like to have advertisment + if user value is above 40
if user_intrest == "YES" and user_advertising == "NO" and user_value_int > 40:
	print("You are " + str(user_value_int) + " worth. Enjoy using our platform")
else:
	print("Your data is nothing worth!! However you can keep using our platform")

	


	