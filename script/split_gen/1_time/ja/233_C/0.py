def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**N):
        num = 1
        for j in range(N):
            if ((i >> j) & 1):
                num *= L[j][1]
            else:
                num *= L[j][2]
        if num <= X:
            ans += 1
    print(ans)
