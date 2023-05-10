def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            B = A[i:j+1]
            if len(B) == M:
                ans = max(ans, sum([k+1 for k in range(M)]) * sum(B))
    print(ans)

if __name__ == '__main__':
    main()