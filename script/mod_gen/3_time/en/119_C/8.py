def solve(N,A,B,C,l):
    if N == 0:
        return 0 if min(A,B,C) > 0 else float('inf')
    ret = float('inf')
    ret = min(ret, solve(N-1,A,B,C,l) + 10)
    ret = min(ret, solve(N-1,A-l[N],B,C,l) + 10)
    ret = min(ret, solve(N-1,A,B-l[N],C,l) + 10)
    ret = min(ret, solve(N-1,A,B,C-l[N],l) + 10)
    return ret
N,A,B,C = map(int,input().split())
l = [int(input()) for _ in range(N)]
print(solve(N,A,B,C,l))

if __name__ == '__main__':
    solve()