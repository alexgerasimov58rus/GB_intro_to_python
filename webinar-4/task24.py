
# ввод исходных данных строкой (1 2 3 4)
bushes = [int(v) for v in input().split(' ')]
n = len(bushes)
max_berries = 0

# пробегаю грядку по "кругу" 
# и ищу максимальный урожай на трех кустах - текущем и соседях
for i in range(n):
    curr = i
    next = (i + 1) % n
    prev = i - 1

    if prev < 0: prev = n - 1

    berries = bushes[prev] + bushes[curr] + bushes[next]
    max_berries = max(berries, max_berries)

print(max_berries)    

