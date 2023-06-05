def f(a, b, c):
    result = -1
    for i in range(a, b+1):
        if i % c == 0:
            result = i
            break
    return result
