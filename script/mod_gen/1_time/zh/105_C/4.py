def base_minus2(n):
    if n == 0:
        return '0'
    else:
        s = ''
        while n != 0:
            m = n % (-2)
            n = n // (-2)
            if m == -1:
                m = 1
                n = n + 1
            s = str(m) + s
        return s
print(base_minus2(int(input())))
