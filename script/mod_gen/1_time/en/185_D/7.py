def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    B = [0]
    for i in range(M):
        B.append(A[i+1] - A[i] - 1)
    B.append(A[0] - 1)
    B.append(N - A[M])
    B.sort()
    ans = 0
    for i in range(len(B)-1):
        ans += B[i]
    print(ans)

if __name__ == '__main__':
    main()