def divisor(n):
    i = 1
    cnt = 0
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                cnt += 1
            else:
                cnt += 2
        i += 1
    return cnt
