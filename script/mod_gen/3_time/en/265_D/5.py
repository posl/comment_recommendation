def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = "No"
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                for l in range(k+1, N):
                    if A[i]+A[j]+A[k]+A[l] == P+Q+R:
                        ans = "Yes"
    print(ans)

if __name__ == '__main__':
    solve()