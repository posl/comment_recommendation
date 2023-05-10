def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**N):
        tmp = 1
        for j in range(N):
            if i & 1<<j:
                tmp *= L[j][0]
        if tmp == X:
            ans += 1
    print(ans)
