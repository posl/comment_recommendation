def get_input():
    x = int(input().strip())
    n = int(input().strip())
    p = []
    if n > 0:
        p = [int(i) for i in input().strip().split()]
    return x, n, p
