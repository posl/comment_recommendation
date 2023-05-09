def main():
    A, B, X = map(int, input().split())
    N = X // A
    if N >= 10**9:
        N = 10**9
    while A * N + B * len(str(N)) > X:
        N -= 1
    print(N)

if __name__ == '__main__':
    main()