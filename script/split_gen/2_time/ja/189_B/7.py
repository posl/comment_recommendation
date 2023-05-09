def main():
    N, X = map(int, input().split())
    ans = -1
    for i in range(N):
        V, P = map(int, input().split())
        X -= V*P/100
        if X < 0:
            ans = i + 1
            break
    print(ans)
