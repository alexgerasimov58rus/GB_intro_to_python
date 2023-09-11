def counting_vowels(phrase):
    vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    count = 0
    for letter in phrase:
        if letter in vowels:
            count += 1

    return count        


song = input('Песенка Пуха: ')
syllable_set = set(map(counting_vowels, song.split()))

if len(syllable_set) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')    
