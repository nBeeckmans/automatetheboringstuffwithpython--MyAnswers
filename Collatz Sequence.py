def collatz(number):
    if number % 2 == 0:
        return number/2 
    elif number %2 == 1:
        return number*3 + 1
      
print('Enter number : ')   



while True :
    Input = input()
    try:
       Input = int(Input)
    except:
        print('Enter an integer')
        continue
    
    while Input > 1:
        Input = collatz(Input)
        print(int(Input))
    break