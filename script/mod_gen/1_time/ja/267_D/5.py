def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(M):
            ans = max(ans, sum(A[i:i+j+1]) + sum(range(1, j+2)))
    print(ans)

if __name__ == '__main__':
    main()