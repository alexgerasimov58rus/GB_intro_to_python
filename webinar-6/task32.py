from random import randint


# размер массива
array_len = randint(10, 20)
# сам массив
array = [randint(-10, 10) for _ in range(array_len)]
# нижняя граница
min_el = randint(-10, 0)
# верхняя граница
max_el = randint(0, 10)

print(f'array_len = {array_len}')
print(f'array = {array}')
print(f'min_el = {min_el}, max_el = {max_el}')

indices = []

for i in range(array_len):
    if min_el <= array[i] <= max_el:
        indices.append(i)

print()
print('indices = ', indices)


