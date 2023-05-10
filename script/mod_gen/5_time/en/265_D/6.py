def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i >= 3:
            break
        for j in range(i+1, N):
            if j >= 3:
                break
            for k in range(j+1, N):
                if k >= 3:
                    break
                for l in range(k+1, N):
                    if l >= 3:
                        break
                    ans = max(ans, P*A[i]+Q*A[j]+R*A[k])
    print(ans)
    return 0

if __name__ == '__main__':
    solve()