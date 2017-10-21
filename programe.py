def show_menu():
    print("1. Ask a Person")
    print("2. View People")
    print("3. Stats")
    print("4. Exit")

    option = input("Enter option: ")
    return option
    
def add_person():
  first_name = input("Enter First Name")
  last_name = input("Enter Last Name")
  team = input("Enter Team")
  age = input("Enter Age")
  
  file = open("people.txt", "a")
  file.write(first_name + "," + last_name + "," + team + "," + age + "\n")
  file.close()
  
def view_people():
    #person_details = {}
    read_people = open("people.txt","r")
    details = [line.split(',') for line in read_people.readlines()]
    for i in details:
        print(i)
    # for i in details:
        # first_name, last_name, team, age = [a.split() for a in i.split(':')]
    # person_details.setdefault(details, []).append(details)
    # print(person_details)
  
def view_stats():
  print("The stats")

def menu_loop():
    while True:
        option = show_menu() #calls the showmenu function and stores the value in option
        if option == "1":
            add_person()
        elif option == "2":
            view_people()
        elif option == "3":
            view_stats()
        elif option == "4":
            break
        else:
            print("Invalid Option")
        print("")
        
menu_loop()