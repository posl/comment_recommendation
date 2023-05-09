def solve():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    x = 0
    for i in range(N):
        if a[i] <= X - x <= b[i]:
            print('Yes')
            exit()
        else:
            x += a[i]
    print('No')

if __name__ == '__main__':
    solve()