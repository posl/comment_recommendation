def solve():
    N, D = map(int, input().split())
    #print(N, D)
    print((N+2*D)//(2*D+1))

if __name__ == '__main__':
    solve()