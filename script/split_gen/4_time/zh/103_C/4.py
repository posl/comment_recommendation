def f(m, a):
    result = 0
    for i in a:
        result += m % i
    return result
