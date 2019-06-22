import math

linha1 = input().split(" ")
linha2 = input().split(" ")

x1, y1 = linha1
x2, y2 = linha2

distancia = math.sqrt(math.pow(float(x2) - float(x1), 2) + math.pow(float(y2)-float(y1),2))

print("%0.4f" %distancia)