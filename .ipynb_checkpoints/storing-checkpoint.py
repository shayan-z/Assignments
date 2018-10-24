import csv

# OPEN CSV FILE
p = open("politicians.csv", "r")



list_count = []

# Function showing data
for count, politician in enumerate(p, 1):

	row 		= politician.strip().split(",")	
	name_p 		= row[0]
	lastname_p 	= row[1]
	birthday_p 	= row[2]
	political_party = row[3]
# 	row = " ".join(row)
# 	print(row)
	full_name_p = name_p + " " + lastname_p # Combine surname + lastname
	
	sentence = str(count) + ": " + full_name_p + " was born in " + birthday_p + " and is a member of the " + political_party
	print(sentence)
	politician = row[0:4]
	list_count.append(politician)

p.close()
	

# def options():


i = 5
while (i == 5):
	options =  input("Select a option: remove, add, save or quit? ").upper()
	if options == "REMOVE":
		question_index_number = input("What is the index number you like to remove? ")
		list_count.pop(int(question_index_number))
		with open('politicians.csv', 'w') as f:
		    writer = csv.writer(f)
		    for row in list_count:
		        writer.writerow(row)
	elif options == "ADD":
		name_p = input("What is name of the politician? ")
		lastname_p = input("What is " + name_p + " lastname? ")
		birthday_p = input("In what year did " + name_p + " born? ")
		political_party = input("Which political party is he member of?")
		with open("politicians.csv", "a") as f:
			writer = csv.writer(f)
			writer.writerow([name_p, lastname_p, birthday_p, political_party])
	elif options == "SAVE":
		with open('politicians.csv', 'w') as f:
		    writer = csv.writer(f)
		    for row in list_count:
		        writer.writerow(row)
	elif options == "QUIT":
		exit()
	else:
		print("wrong option")
	
# options()








