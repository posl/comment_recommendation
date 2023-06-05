def solve():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)
    # print(X)
    sum = 0
    for i in range(N):
        if (i+1) % 2 == 0:
            sum += b[i]
        else:
            sum += a[i]
    if sum >= X:
        print('Yes')
    else:
        print('No')
