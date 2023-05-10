def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    t = 0
    for A, B in AB:
        t += A / B
    t /= 2
    x = 0
    for A, B in AB:
        if t > A / B:
            t -= A / B
            x += A
        else:
            x += B * t
            break
    print(x)
