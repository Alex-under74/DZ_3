while True:
    sequence = (input('Введите последовательность чисел(в качестве разделителя используйте запятую,'
                      'точку с запятой или слэш, но выберите что-то одно): '))


    if ',' in sequence and ';' not in sequence and '/' not in sequence:
        sequence = str(set(int(i) for i in list(sequence.split(','))))
        print(sequence[1:-1])
        break
    elif ';' in sequence and ',' not in sequence and '/' not in sequence:
        sequence = str(set(int(i) for i in list(sequence.split(';'))))
        print(sequence[1:-1])
        break
    elif '/' in sequence and ',' not in sequence and ';' not in sequence:
        sequence = str(set(int(i) for i in list(sequence.split('/'))))
        print(sequence[1:-1])
        break
    else:
        print('Ну я же говорил! Используй только один разделитель!! Пробуй еще разок')

