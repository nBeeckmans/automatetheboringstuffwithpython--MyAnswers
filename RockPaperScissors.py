import random,sys

win_counter = 0
lose_counter = 0
tie_counter = 0 
acceptable_input = ['R','r','p','P','s','S','q','Q']

while True:
    print ('%s wins, %s losses, %s ties' %(win_counter,lose_counter,tie_counter))
    while True: 
        print('Play (r)ock,(p)aper,(s)cissors or (q)uit')
        user_input = input()
        if user_input == 'q' or user_input == 'Q':
            sys.exit()
        elif user_input in acceptable_input :
            break
        else :
            print('You lied')
    #beepboop
    if user_input == 'r' or user_input == 'R':
        print('Rock versus...')   
        user_input = 'r'
    elif user_input == 'p' or user_input == 'P':
        print('Paper versus...')
        user_input  = 'p'
    elif user_input == 's' or user_input == 'S':
        print('Scissor versus...')
        user_input = 's'
   #inchallah
    PC_rand = random.randint(1,3)
    if PC_rand == 1:
        print('Rock')
    elif PC_rand == 2:
        print('Paper')
    elif PC_rand == 3:
        print('Scissor')
    #BRUUUUUUUUUH
    if user_input == 'r':
        if PC_rand == 1:
            tie_counter += 1
            print('Ties...') 
        elif PC_rand == 3:
            win_counter += 1
            print('WIN!!')
        elif PC_rand == 2: 
            lose_counter += 1 
            print('LOSER AHAHAHAH') 

 
    if user_input == 'p':
        if PC_rand == 2:
            tie_counter += 1
            print('Ties...') 
        elif PC_rand == 1:
            win_counter += 1
            print('WIN!!')
        elif PC_rand == 3: 
            lose_counter += 1 
            print('LOSER AHAHAHAH')  
   
    if user_input == 's':
        if PC_rand == 3:
            tie_counter += 1
            print('Ties...') 
        elif PC_rand == 2:
            win_counter += 1
            print('WIN!!')
        elif PC_rand == 1: 
            lose_counter += 1 
            print('LOSER AHAHAHAH')                        