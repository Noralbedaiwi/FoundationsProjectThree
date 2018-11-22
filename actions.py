# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Nora"
my_age = 29
my_bio = ""
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    print("Would you like to:")
    print("1) Create a new club.\n or:")
    print("2) Browse and join club\n or:")
    print("3) View existing clubs.\n or:")
    print("4) Display members of a club.\n or:")
    print("-1) Close application.")
    user_option = input("> ")
    return user_option
    
def print_population():
	index = 1
	for person in population:
		print("[%s] %s" % (index, person.name))
		index += 1

def create_club():
    # your code goes here!
    club_name = input("Pick a name for your awesome new club: ")
    club_description = input("What is your club about?\n")
    club = Club(club_name, club_description)
    club.recruit_member(myself)
    club.assign_president(myself)
    print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop): ")
    print_population()
    person_to_be_recruited = ""
    while person_to_be_recruited != "-1":
    	person_to_be_recruited = input("> ")
    	club.recruit_member(population[int(person_to_be_recruited)-1])
    print("Here's your new club...")
    print(club.name)
    print(club.description)
    club.print_member_list()
    clubs.append(club)		

def view_clubs():
    # your code goes here!
    for club in clubs:
    	print("\tName: %s\n\tDescription: %s\n\tMembers: %s\n" % (club.name, club.description, len(club.member)))


def view_club_members():
    # your code goes here!
    view_clubs()
    club_found = False
    while not club_found:
	    club_name = input("Enter the name of the club whose members you'd like to see: ")
	    for club in clubs:
	    	if club.name.lower() == club_name.lower():
	    		club.print_member_list()
	    		club_found = True
	    

def join_clubs():
    # your code goes here!
    view_clubs()
    club_found = False
    while not club_found:
	    club_name = input("Enter the name of the club you'd like to join: ")
	    for club in clubs:
	    	if club.name.lower() == club_name.lower():
	    		club.recruit_member(myself)
	    		club_found = True
    

def application():
    introduction()
    # your code goes here!
    option = ""
    while option != "-1":
    	option = options()
    	if option == "1":
    		create_club()
    	elif option == "2":
    		join_clubs()
    	elif option == "3":
    		view_clubs()
    	elif option == "4":
    		view_club_members()
    	elif option == "-1":
    		break