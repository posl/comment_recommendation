def main():
    # input
    N, Q = map(int, input().split())
    x = []
    for _ in range(Q):
        x.append(int(input()))
    # compute
    a = list(range(1, N+1))
    for i in range(Q):
        if i == 0:
            a[0], a[1] = a[1], a[0]
        else:
            if a.index(x[i]) == 0:
                a[0], a[1] = a[1], a[0]
            else:
                a[a.index(x[i])], a[a.index(x[i])-1] = a[a.index(x[i])-1], a[a.index(x[i])]
    # output
    print(*a)
