def problem125_a(a, b, t):
    count = 0
    for i in range(1, t + 1):
        if i % a == 0:
            count += 1
    return count * b
