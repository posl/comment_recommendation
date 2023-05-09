def main():
    N, L = map(int, input().split())
    A = [L + i - 1 for i in range(1, N + 1)]
    if L <= 0 <= L + N - 1:
        print(sum(A))
    elif L + N - 1 < 0:
        print(sum(A) - A[-1])
    else:
        print(sum(A) - A[0])

if __name__ == '__main__':
    main()