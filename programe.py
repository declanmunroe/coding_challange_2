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
    read_people = open("people.txt","r")
    details = [line.split(',') for line in read_people.readlines()]
    count = 0
    for i in details:
        count += 1
        i[-1] = i[-1].strip()
        
    details_avg = [age[3] for age in details]
    sum_list = sum(map(int, details_avg))
    average_age = sum_list / count
    print("There are : {} people stored with an average age of {}".format(count, average_age))
    
def team_average_age():
    with open("people.txt", "r") as f:
        d = {}
        for line in f.readlines():
            line = line.split(',')
            
            key = line[2].strip()
            value = line[3].strip()
            
            if key in d:
              d[key].append(value)
            else:
              d[key] = [value]
              
    #team_age_total = 0
    for key, value in d.items():
        print(key, value)
    
    
    
    
def menu_loop():
    while True:
        option = show_menu() #calls the showmenu function and stores the value in option
        if option == "1":
            add_person()
        elif option == "2":
            view_people()
        elif option == "3":
            view_stats()
            team_average_age()
        elif option == "4":
            break
        else:
            print("Invalid Option")
        print("")
        
menu_loop()