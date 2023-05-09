def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i + M <= N:
            ans = max(ans, sum([sum(A[i:i+M][::-1][j:]) for j in range(M)]))
    print(ans)

if __name__ == '__main__':
    main()