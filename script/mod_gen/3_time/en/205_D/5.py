def solve():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    K = [int(input()) for _ in range(Q)]
    for k in K:
        ok = 10**18
        ng = 0
        while ok-ng>1:
            mid = (ok+ng)//2
            if check(mid,A,k):
                ok = mid
            else:
                ng = mid
        print(ok)

if __name__ == '__main__':
    solve()