cat = input('Введите категорию товара: ')
if cat == 'продукты':
	s = int(input('Введите цену товара: '))
	if s<100: print('Попробуйте нашу выпечку!')
	elif s>100 and s<500: print('Как насчёт орехов в шоколаде?')
	else: print('Попробуйте экзотические фрукты!')
else: print('Загляните в товары для дома!')
