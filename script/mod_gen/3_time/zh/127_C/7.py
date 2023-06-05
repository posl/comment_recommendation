def solve():
    N,M = map(int,input().split())
    L = []
    R = []
    for i in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(max(0,R[0]-L[-1]+1))

if __name__ == '__main__':
    solve()