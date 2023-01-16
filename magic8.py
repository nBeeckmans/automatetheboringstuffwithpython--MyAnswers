import random,time 

phrases = ['ok','kek','bruh','idk','wth','wtf']

while True:
    try:
        print(phrases[random.randint(0,len(phrases)-1)])
        time.sleep(0.5)
    except KeyboardInterrupt :
        break 