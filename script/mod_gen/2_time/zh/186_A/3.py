def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    white = []
    for i in range(M+1):
        if A[i] != 1:
            white.append(A[i]-1)
    white.sort()
    if len(white) == 0:
        print(0)
        return
    k = white[0]
    ans = 0
    for i in range(M+1):
        ans += (A[i]-1)//k
        if (A[i]-1) % k != 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()