def main():
    N, X = map(int, input().split())
    for i in range(N):
        v, p = map(int, input().split())
        X -= v * p / 100
        if X < 0:
            print(i + 1)
            return
    print(-1)
