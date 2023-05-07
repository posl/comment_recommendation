def main():
    N, M = map(int, input().split())
    A = [0] * M
    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(1, a[0] + 1):
            A[a[j] - 1] += 1
    print(A.count(N))

if __name__ == '__main__':
    main()