def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    mod = T % total
    for i in range(N):
        if mod >= A[i]:
            mod -= A[i]
        else:
            print(i + 1, mod + A[i])
            return

if __name__ == '__main__':
    main()