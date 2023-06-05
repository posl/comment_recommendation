def solve(N):
    ans = 0
    for A in range(1,N+1):
        for B in range(A,N+1):
            if A*B>N:
                break
            for C in range(B,N+1):
                if A*B*C<=N:
                    ans+=1
                else:
                    break
    return ans

if __name__ == '__main__':
    solve()