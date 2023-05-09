def f(n, a, b):
    #print(n, a, b)
    min_a = max(a)
    max_b = min(b)
    if min_a > max_b:
        return 0
    else:
        return max_b - min_a + 1

if __name__ == '__main__':
    f()