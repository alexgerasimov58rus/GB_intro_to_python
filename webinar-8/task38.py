import os


def read_phone_book():
    if not os.path.exists('phone_book.txt'):
        with open('phone_book.txt', 'w'): 
            pass
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        return file.read().split('\n')[:-1]


def write_phone_book(abonents):
    with open('phone_book.txt', 'w', encoding='utf-8') as file:
        for abonent in abonents:
            file.write(abonent + '\n')    


def print_phone_book(abonents):
    if len(abonents) == 0:
        print('в книге нет записей')
        return
    
    for i in range(len(abonents)):
        surname, name, phone = abonents[i].split(':')
        print(f'{i + 1}.\t {surname} {name}: {phone}')     


def add_entry(abonents):
    name = input('введите имя: ')
    surname = input('введите фамилию: ')
    phone = input('введите номер телефона: ')
    abonents.append(f'{surname}:{name}:{phone}')
    abonents.sort() 


def search_entries(abonents):
    search = input('Введите строку для поиска: ')
    for i in range(len(abonents)):
        if search.lower() in abonents[i].lower():
            surname, name, phone = abonents[i].split(':')
            print(f'{i + 1}.\t {surname} {name}: {phone}') 


def delete_entry(abonents):
    print('выберите номер записи для удаления из диапазона: ', 1, ' - ', len(abonents))
    print('для отмены действия, введите любой другой символ')
    index = input('номер записи: ')
    if index in [str(i + 1) for i in range(len(abonents))]:
        del abonents[int(index) - 1]            


def change_entry(abonents):
    print('выберите номер записи для изменения из диапазона: ', 1, ' - ', len(abonents))
    print('для отмены действия, введите любой другой символ')   
    index = input('номер записи: ')     
    if index in [str(i + 1) for i in range(len(abonents))]:
        index = int(index) - 1
        surname, name, phone = abonents[index].split(':')
        
        new_name = input(f'введите имя({name}): ')
        if new_name:
            name = new_name

        new_surname = input(f'введите фамилию({surname}): ')
        if new_surname:
            surname = new_surname
        
        new_phone = input(f'введите номер телефона({phone}): ')
        if new_phone:
            phone = new_phone
        
        abonents[index] = f'{surname}:{name}:{phone}'
        abonents.sort()


def user_interface():
    abonents = read_phone_book()
    choice = '1'

    while choice != '0':
        print('''Выберите действие: 
                1 - вывести данные
                2 - добавить запись
                3 - поиск записей
                4 - удалить запись
                5 - изменить запись
                0 - выход''')
    
        choice = input('номер действия: ')
        
        if choice not in ('1', '2', '3', '4', '5', '0'):
            print('некорректный ввод')
            continue

        match(choice):
            case '0': print('всего доброго')
            case '1': print_phone_book(abonents) 
            case '2': add_entry(abonents)
            case '3': search_entries(abonents)   
            case '4': delete_entry(abonents)
            case '5': change_entry(abonents)
    
    write_phone_book(abonents)    


user_interface()