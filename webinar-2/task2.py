
# функция поиска чисел полным перебором
def findXY(S, P):
    for X in range(1, 1001):
        for Y in range(1, 1001):
            if X + Y == S and X * Y == P:
                return (X, Y)

# ввод исходных данных строкой (4 4)
N = [int(v) for v in input().split(' ')]
S = N[0] # S = X + Y
P = N[1] # P = X * Y

XY = findXY(S, P)

print(XY[0], XY[1])