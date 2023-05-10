def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        i = 0
        j = N
        while j - i > 1:
            k = (i + j) // 2
            if A[k] >= x:
                j = k
            else:
                i = k
        print(N - j)

if __name__ == '__main__':
    main()