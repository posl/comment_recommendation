def lunlun(k):
    if k <= 9:
        return k
    k -= 9
    digits = 2
    while True:
        if k <= 9 * 10 ** (digits - 1):
            break
        k -= 9 * 10 ** (digits - 1)
        digits += 1
    for i in range(10 ** (digits - 1), 10 ** digits):
        if k <= get_count(i):
            return i
        k -= get_count(i)
