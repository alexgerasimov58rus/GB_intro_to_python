
# в вводе n,m смысла не вижу - только путают
# n, m = [int(v) for v in input().split(' ')]

# ввод первого множества строкой (2 4 6 8 10 12 10 8 6 4 2)
n_set = set([int(v) for v in input().split(' ')])
# ввод второго множества строкой (3 6 9 12 15 18)
m_set = set([int(v) for v in input().split(' ')])

# результат пересечения множеств
i_set = n_set & m_set

print(*sorted(list(i_set)))



