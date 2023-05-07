def solve():
    N = int(input())
    x = 1
    y = 1
    for i in range(N-1):
        if x < y:
            x += 1
        else:
            y += 1
    print(x+y-2)
    return
