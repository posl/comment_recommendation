def main():
    N, L = map(int, input().split())
    A = [L + i - 1 for i in range(1, N + 1)]
    if 0 in A:
        print(sum(A))
    elif L >= 0:
        print(sum(A) - A[0])
    elif L < 0 and L + N - 1 >= 0:
        print(sum(A))
    else:
        print(sum(A) - A[-1])

if __name__ == '__main__':
    main()