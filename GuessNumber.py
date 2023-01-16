import random

number_to_guess = random.randint(1,20)

print('Guess the number (1 to 20) !')

while True:
    user_input = input()
    if user_input.isdigit() == False:
        print('please enter a number !')
        continue
    user_input = int(user_input)
    if user_input > 20 or user_input < 1:
        print('input is out of bound please try again')
    else :
        if user_input == number_to_guess :
            break;
        elif user_input < number_to_guess :
            print('try a bigger number !')
        elif user_input > number_to_guess:
            print('try a smaller number !')

print('Great ! You correctly found the number : ' + str(number_to_guess))


