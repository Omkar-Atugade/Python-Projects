known_users = ['Omkar' ,'Vishal', 'Vikrant' ,'Gaurav' ,'Sayali' ,'Trupti' ,'Nandani']

x = 'Atugade'

while True:

    print("Hi! My name is Omkar")
    
    name = input('What is your name ? : ').strip().capitalize()

    if name in known_users:
        print('Hello {}!'.format(name))

        remove = input("Would you like to be removed from the system (y/n)? :").lower()

        if remove == 'y' :
            known_users.remove(name)
        elif remove == 'n' :
            print("No problem, I didn't want you to leave anyway!")

    else:
        print("Sorry , I don't think I have met you yet {}".format(name))
        
        add = input("Would you like to be added to the system (y/n)? :").lower()

        if add == 'y' :
            check = input('Enter My sirname :').strip().capitalize()

            if check == x :
                known_users.append(name)
                print('Conragulation! Your name is added to the system.')
                
            else:
                print('Sorry try again.')

        elif add == 'n' :
            print('No worries, see you around!')

