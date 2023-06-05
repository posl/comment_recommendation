def solve():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(N):
        if X < a[i] or X > b[i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    solve()