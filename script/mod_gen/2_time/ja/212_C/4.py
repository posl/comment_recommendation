def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    a = 0
    b = 0
    ans = 1000000000000000000
    while a < N and b < M:
        if A[a] < B[b]:
            ans = min(ans,abs(A[a] - B[b]))
            a += 1
        else:
            ans = min(ans,abs(A[a] - B[b]))
            b += 1
    print(ans)

if __name__ == '__main__':
    main()