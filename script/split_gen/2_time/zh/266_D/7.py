def main():
    n = int(input())
    txa = []
    for i in range(n):
        txa.append(list(map(int, input().split())))
    res = 0
    for i in range(n):
        if i == 0:
            res += txa[i][2]
            continue
        res += txa[i][2]
        if txa[i][1] == txa[i-1][1]:
            continue
        elif txa[i][1] > txa[i-1][1]:
            res -= txa[i][0]-txa[i-1][0]
        else:
            res -= txa[i][0]-txa[i-1][0]
    print(res)
