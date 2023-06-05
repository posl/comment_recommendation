def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(N):
        A[i] = A[i] % M
    for i in range(N):
        if A[i] == 0:
            break
        if i == N - 1:
            ans += A[i]
            break
        if A[i] == A[i + 1] or A[i] == A[i + 1] + 1:
            A[i + 1] = 0
        else:
            ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()