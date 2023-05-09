def main():
    N, X = map(int, input().split())
    L = [[int(x) for x in input().split()] for i in range(N)]
    ans = 0
    for i in range(2**N):
        tmp = 1
        for j in range(N):
            if i >> j & 1:
                tmp *= L[j][1 + i >> j & 1]
        if tmp == X:
            ans += 1
    print(ans)
