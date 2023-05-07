def main():
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(2*N)]
    ans = [i for i in range(1, 2*N+1)]
    for i in range(M):
        for j in range(N):
            a = ans[2*j]
            b = ans[2*j+1]
            if A[a-1][i] == A[b-1][i]:
                continue
            elif (A[a-1][i] == 'G' and A[b-1][i] == 'C') or (A[a-1][i] == 'C' and A[b-1][i] == 'P') or (A[a-1][i] == 'P' and A[b-1][i] == 'G'):
                ans[2*j], ans[2*j+1] = ans[2*j+1], ans[2*j]
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()