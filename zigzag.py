import time,sys

i = 0
increasing = True
try:
    while True:
        print(' '*i, end='')
        print('********')
        time.sleep(0.1)

        if increasing == True:
            i += 1
            if i == 20:
                increasing = False
        elif increasing == False:
            i -= 1 
            if i == 0: 
                increasing = True
except KeyboardInterrupt:
    sys.exit() 