def convert_to_base2(n):
    if n == 0:
        return '0'
    result = ''
    while n != 0:
        remainder = n % (-2)
        n = n // (-2)
        if remainder < 0:
            remainder += 2
            n += 1
        result = str(remainder) + result
    return result
