count = 0
for i in range(0,5):    
    x = int(input())
    if x % 2 == 0:
        count += 1

print('{} valores pares'.format(count))
