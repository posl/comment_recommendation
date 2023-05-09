def divisor(n):
    i = 1
    result = []
    while i*i <= n:
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n//i)
        i += 1
    result.sort()
    return result
