def main():
    A, B, X = map(int, input().split())
    if X < A:
        print(0)
        return
    if A * 10**9 + B * 10 <= X:
        print(10**9)
        return
    N = 1
    while A * N + B * len(str(N)) <= X:
        N *= 10
    N //= 10
    while A * N + B * len(str(N)) <= X:
        N += 1
    print(N - 1)

if __name__ == '__main__':
    main()