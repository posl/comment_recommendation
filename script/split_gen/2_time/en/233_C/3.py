def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 1 << N):
        flag = True
        mul = 1
        for j in range(N):
            if (1 << j) & i:
                mul *= L[j][1 + (i >> j) % L[j][0] - 1]
                if mul > X:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)
