def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] + A[j] + A[k] <= P:
                    ans = max(ans, (A[i] + A[j] + A[k]) * Q)
                else:
                    break
    print(ans)

if __name__ == '__main__':
    main()