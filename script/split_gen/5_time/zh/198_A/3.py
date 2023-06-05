def share_candy(num):
    if num < 3:
        return 0
    elif num % 2 == 0:
        return int(num/2) - 1
    else:
        return int(num/2)
