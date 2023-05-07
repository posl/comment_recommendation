def main():
    N, M = map(int, input().split())
    A = [0] * (N + 1)
    for i in range(M):
        l, r = map(int, input().split())
        A[l - 1] += 1
        A[r] -= 1
    for i in range(N):
        A[i + 1] += A[i]
    print(A.count(M))

if __name__ == '__main__':
    main()