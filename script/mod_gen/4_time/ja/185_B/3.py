def solve():
    # coding: utf-8
    # Your code here!
    n,m,t = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    #print(a)
    #print(b)
    bat = n
    #print(bat)
    for i in range(m):
        bat = bat - (a[i] - b[i-1])
        if bat <= 0:
            print("No")
            return
        bat = bat + (b[i] - a[i])
        if bat > n:
            bat = n
        #print(bat)
    bat = bat - (t - b[m-1])
    if bat <= 0:
        print("No")
        return
    print("Yes")
    return

if __name__ == '__main__':
    solve()