def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    need = N * M - sumA
    if need <= 0:
        print(0)
    elif need <= K:
        print(need)
    else:
        print(-1)

if __name__ == '__main__':
    main()