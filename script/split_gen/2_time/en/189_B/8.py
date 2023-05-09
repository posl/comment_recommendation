def main():
    N, X = map(int, input().split())
    for i in range(1, N+1):
        V, P = map(int, input().split())
        X -= V * P/100
        if X < 0:
            print(i)
            exit()
    print(-1)
