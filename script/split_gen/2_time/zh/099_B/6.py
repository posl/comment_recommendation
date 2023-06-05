def snow(a, b):
    # 雪覆盖的深度
    x = 0
    # 求和
    sum = 0
    for i in range(1, 1000):
        sum += i
        if sum >= a:
            # 雪覆盖的深度
            x = i
            break
    return x
