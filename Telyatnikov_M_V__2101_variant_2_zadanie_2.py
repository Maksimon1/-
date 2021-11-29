n = int (input ('Введите количество положительных чисел: '))
zna4enie = 0
summa = 0
for i in range (1, n+1):
    zna4enie=(i*(i+1))/2
    summa +=zna4enie
print ('Сумма первых', n, 'чисел равна', int(summa))
