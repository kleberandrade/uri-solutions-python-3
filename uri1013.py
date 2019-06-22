valor = input().split(" ")
a, b, c = valor

maiorAB = ((int(a) + int(b)) + abs(int(a) - int(b)))/2
maiorAC = ((int(a) + int(c)) + abs(int(a) - int(c)))/2
maior = ((maiorAB + maiorAC) + abs(maiorAB - maiorAC))/2

print("%d eh o maior" % maior)