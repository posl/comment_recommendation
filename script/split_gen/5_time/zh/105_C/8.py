def get_base_2(num):
    if num == 0:
        return "0"
    result = ""
    while num != 0:
        temp = num % (-2)
        num = num // (-2)
        if temp < 0:
            temp += 2
            num += 1
        result = str(temp) + result
    return result
