def split(num):
    num = str(num)
    length = len(num)
    if length == 1:
        return 0
    if length == 2:
        return int(num[0]) * int(num[1])
    max = 0
    for i in range(1, length):
        num1 = num[0:i]
        num2 = num[i:length]
        if num1[0] == '0' or num2[0] == '0':
            continue
        product = int(num1) * int(num2)
        if product > max:
            max = product
    return max
