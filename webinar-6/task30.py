import random

# первый элемент
first_el = random.randint(0, 10)
# шаг прогрессии
step = random.randint(1, 5)
# количество элементов
count = random.randint(5, 10)

print(f'first_el = {first_el} step = {step} count = {count}')

result = [first_el + i * step for i in range(count)]
print(result)
print(list(range(first_el, first_el + count * step, step)))

# for _ in range(count):
#     print(first_el, end=' ')
#     first_el += step

