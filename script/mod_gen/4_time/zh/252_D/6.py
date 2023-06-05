def solve(N, A):
    # 请在此添加代码
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    cnt += 1
    return cnt

if __name__ == '__main__':
    solve()