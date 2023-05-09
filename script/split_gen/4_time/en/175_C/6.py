def problems175_c():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k*d:
        print(x - k*d)
    else:
        if (k*d - x) % (2*d) == 0:
            print(0)
        else:
            print(min(abs(x - (k*d - x) % (2*d)), abs(x - (k*d - x) % (2*d) - 2*d)))
