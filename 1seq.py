dlina_spiska = int(input('Введите количество элементов: '))
spisok = []

for i in range(dlina_spiska):
    spisok.append(int(input(f'Введите элемент номер {i + 1}: ')))

spisok.sort()

print(spisok)
