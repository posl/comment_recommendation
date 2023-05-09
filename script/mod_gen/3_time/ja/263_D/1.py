def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        if A[i] < L:
            sum += L
        elif A[i] > R:
            sum += R
        else:
            sum += A[i]
    print(sum)

if __name__ == '__main__':
    main()