def problem190_a():
    a, b, c = map(int, input().split())
    if c == 0:
        a -= 1
        if a >= b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        b -= 1
        if b >= a
