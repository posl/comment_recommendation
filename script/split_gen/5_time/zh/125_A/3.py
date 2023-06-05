def problem125_a():
    A, B, T = map(int, input().split())
    result = 0
    for i in range(T):
        if (i + 1) % A == 0:
            result += B
    print(result)
