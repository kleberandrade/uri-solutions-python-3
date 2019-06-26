count = 0
total = 0.0
for i in range(0,6):    
    x = float(input())
    if x > 0:
        count += 1
        total += x

print('{} valores positivos'.format(count))
print('%.1f' % (total / count))
