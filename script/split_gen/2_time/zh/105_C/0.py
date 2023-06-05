def base2_m2(n):
    if n == 0:
        return '0'
    else:
        ans = ''
        while n != 0:
            if n % (-2) == 0:
                ans = '0' + ans
                n = n // (-2)
            else:
                ans = '1' + ans
                n = (n - 1) // (-2)
        return ans
