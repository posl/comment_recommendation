def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    x = T % total
    for i in range(N):
        if x <= A[i]:
            print(i + 1, x)
            break
        x -= A[i]

if __name__ == '__main__':
    main()