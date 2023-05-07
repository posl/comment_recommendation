def main():
    N, M = [int(x) for x in input().split()]
    cakes = []
    for i in range(N):
        cakes.append([int(x) for x in input().split()])
    ans = 0
    for i in range(8):
        tmp = 0
        for j in range(N):
            tmp += max(cakes[j][0] if i & 1 == 0 else -cakes[j][0],
                       cakes[j][1] if i & 2 == 0 else -cakes[j][1],
                       cakes[j][2] if i & 4 == 0 else -cakes[j][2])
        ans = max(ans, tmp)
    print(ans)
