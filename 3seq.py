first_seq = set([int(i) for i in input('Введите элементы первого множества через запятую: ').split(',')])

second_seq = set([int(i) for i in input('Введите элементы второго множества через запятую: ').split(',')])

print(str(first_seq.symmetric_difference(second_seq))[1:-1])

