def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(M)
    B = []
    for i in range(N):
        if A[i+1] - A[i] >= 2:
            B.append(A[i+1] - A[i] - 1)
    if len(B) == 0:
        print(0)
        return
    B.sort()
    B.append(M)
    ans = 0
    for i in range(len(B)-1):
        ans += B[i] * (i+1)
    print(ans)

if __name__ == '__main__':
    main()