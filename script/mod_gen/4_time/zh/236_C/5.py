def solve():
    N,M = map(int,input().split())
    S = input().split()
    T = input().split()
    for s in S:
        if s in T:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    solve()