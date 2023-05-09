def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-4):
        for j in range(i+1, N-3):
            for k in range(j+1, N-2):
                for l in range(k+1, N-1):
                    ans = max(ans, P*A[i] + Q*A[j] + R*A[k] + A[l])
    print(ans)

if __name__ == '__main__':
    main()