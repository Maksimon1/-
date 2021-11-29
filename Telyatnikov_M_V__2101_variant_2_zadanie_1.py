from math import tan, pi

s = float (input ('Введите длину стороны: '))
n = int (input ('Введите количество сторон: '))
area = (n * s ** 2) / (4 * tan(pi / n))
print ('Площадь правильного многоугольника равна', round(area,2))
