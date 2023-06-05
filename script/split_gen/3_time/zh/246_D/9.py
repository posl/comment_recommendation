def f(n):
    if n < 2:
        return n
    else:
        a = 1
        b = n
        while abs(a - b) > 1:
            m = (a + b) // 2
            if m**3 + m**2*m + m*m**2 + m**3 < n:
                a = m
            else:
                b = m
        return b
print(f(int(input())))
