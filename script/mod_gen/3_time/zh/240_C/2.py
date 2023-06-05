def solve():
    N,X = map(int,input().split())
    a = [0]*N
    b = [0]*N
    for i in range(N):
        a[i],b[i] = map(int,input().split())
    if X < min(a):
        print('No')
        return
    if X >= max(b):
        print('Yes')
        return
    print('No')
    return

if __name__ == '__main__':
    solve()