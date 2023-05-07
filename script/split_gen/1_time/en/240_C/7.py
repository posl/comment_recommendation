def solve():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    total = 0
    for i in range(N):
        if i % 2 == 0:
            total += a[i]
        else:
            total += b[i]
    if total <= X:
        print("Yes")
    else:
        print("No")
