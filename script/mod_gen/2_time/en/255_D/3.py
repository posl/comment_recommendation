def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        i = 0
        j = N - 1
        while i < j:
            if A[i] < x:
                i += 1
            else:
                j -= 1
        if A[i] < x:
            print(2 * (x - A[i]) + N)
        else:
            print(N)

if __name__ == '__main__':
    main()