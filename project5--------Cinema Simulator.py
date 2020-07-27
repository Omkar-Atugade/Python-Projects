films = {
        'DDLJ' : [3 ,5],
        'ADHM': [18, 7],
        'ZNMD': [15, 20],
        'ROCSTAR' : [12, 80],
        'TAMASHA' : [18, 55],
        'AJHD' : [18, 2]
        }

while True :

    choice = input("Enter the film you want to watch ? :").strip().upper()

    if choice in films:
        age = int(input('How old are you ? :').strip())

        if age >= films[choice][0] :
            x = films[choice][1]
            num = int(input('How many tickets do you want ? :').strip())
            
            if num <= x:
                print('Enjoy the film!')
                films[choice][1]= films[choice][1] -1
            else :
                print("Sorry! We don't have that many tickets. Try with less number.")
        else :
            print('You are too young to see that film!')
    else:
        print("We don't have that film......")
        
    
    
    
