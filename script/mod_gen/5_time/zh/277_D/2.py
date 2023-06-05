def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    a = 0
    for i in range(N):
        if A[i] >= M//2:
            a = i
            break
    A = A[a:]
    N = len(A)
    for i in range(N):
        A[i] %= M
    ans = 0
    for i in range(N):
        if i == 0:
            ans += A[i]
            continue
        if A[i] - A[i-1] <= 1:
            continue
        ans += A[i-1]+1
    print(ans)

if __name__ == '__main__':
    main()