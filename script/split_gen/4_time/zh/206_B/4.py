def problem206_b():
    N = int(input())
    x = 0
    sum = 0
    while sum < N:
        x += 1
        sum += x
    print(x)
problem206_b()
