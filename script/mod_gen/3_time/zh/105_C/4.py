def base_m2(num):
    result = []
    while num != 0:
        if num % (-2) == 0:
            result.append(0)
            num = num // (-2)
        else:
            result.append(1)
            num = (num - 1) // (-2)
    result.reverse()
    return result

if __name__ == '__main__':
    base_m2()