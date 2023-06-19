def solve(A,B,N):
    ans = 0
    x = min(B-1,N)
    ans = (A*x)//B - A*(x//B)
    return ans

if __name__ == '__main__':
    solve()