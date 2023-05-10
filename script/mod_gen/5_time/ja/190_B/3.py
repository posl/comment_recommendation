def solve():
    n,s,d = map(int,input().split())
    for _ in range(n):
        x,y = map(int,input().split())
        if x < s and y > d:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    solve()