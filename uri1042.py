entradas = input().split()
valores = [int(i) for i in entradas]
valores.sort()

print(*valores, sep='\n')
print()
print(*entradas, sep='\n')