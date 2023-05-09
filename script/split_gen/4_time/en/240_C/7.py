def solve():
    N,X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    pos = 0
    for i in range(N):
        pos += a[i]
        if pos > X:
            print("No")
            return
        pos += b[i]
    if pos > X:
        print("No")
        return
    print("Yes")
