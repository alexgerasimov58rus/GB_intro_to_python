
# ввод исходных данных строкой (0 1 0 0 1 0)
coins = input().split(' ')
count_0 = 0
count_1 = 0

for c in coins:
    if c == '0': count_0 += 1
    if c == '1': count_1 += 1

print(min(count_0, count_1))    