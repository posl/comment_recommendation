def find_kth_0_2_number(k):
    # 2是第一个数
    if k == 1:
        return 2
    # 20是第二个数
    if k == 2:
        return 20
    # 22是第三个数
    if k == 3:
        return 22
    # 从第四个数开始，每次加2
    k -= 3
    num = 22
    while k > 0:
        num += 2
        if '1' not in str(num) and '3' not in str(num) and '4' not in str(num) and '5' not in str(num) and '6' not in str(num) and '7' not in str(num) and '8' not in str(num) and '9' not in str(num):
            k -= 1
    return num
