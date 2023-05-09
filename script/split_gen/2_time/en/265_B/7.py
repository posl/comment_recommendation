def problems265_b():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(m):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    t_ = t
    n_ = n
    for i in range(n-1):
        if t_ > 0:
            t_ -= a[i]
            if t_ > 0:
                n_ -= 1
                if n_ in x:
                    t_ += y[x.index(n_)]
            else:
                break
    if n_ == 1:
        print('Yes')
    else:
        print('No')
