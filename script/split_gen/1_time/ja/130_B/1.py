def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 1
    d = 0
    for i in range(N):
        d += L[i]
        if d > X:
            break
        ans += 1
    print(ans)
