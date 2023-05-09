def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i] // (2**M)
        A[i] %= 2**M
        A.sort(reverse=True)
        for j in range(M):
            if A[i] == 0:
                break
            A[i] //= 2
            A.sort(reverse=True)
    print(ans)

if __name__ == '__main__':
    main()