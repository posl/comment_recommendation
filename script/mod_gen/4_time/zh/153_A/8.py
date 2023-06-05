def problems153_a():
    h, a = map(int, input().split())
    if h % a == 0:
        print(h // a)
    else:
        print(h // a + 1)
problems153_a()
