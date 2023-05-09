def problem281_c():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    print(t // sum(a) + 1, t % sum(a) + 1)
