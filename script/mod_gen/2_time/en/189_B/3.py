def main():
    N, X = map(int, input().split())
    for i in range(N):
        v, p = map(int, input().split())
        X -= v * p / 100
        if X < 0:
            return i + 1
    return -1
print(main())
