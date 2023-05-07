def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = sum(A)
    for i in range(N):
        ans -= A[i] // (2**M)
    print(ans)

if __name__ == '__main__':
    main()