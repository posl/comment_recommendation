def g_1(x):
    digits = [int(d) for d in str(x)]
    digits.sort(reverse=True)
    return int(''.join(str(d) for d in digits))
