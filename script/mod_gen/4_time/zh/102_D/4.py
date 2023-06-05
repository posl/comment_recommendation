def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10**9
    for i in range(1, N):
        for j in range(i+1, N):
            P = sum(A[:i])
            Q = sum(A[i:j])
            R = sum(A[j:j+1])
            S = sum(A[j+1:])
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
    print(ans)

if __name__ == '__main__':
    main()