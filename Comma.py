spam = []
for i in range(20):
    spam.append(i + 1)

for i in range(len(spam)):
    print(spam[i], end='')
    if i == len(spam):
        continue
    elif i == len(spam) -2:
        print(' and ', end='')
    elif i == len(spam) - 1:
        print()
    else:
        print(', ', end= '')  
    
