def jump(n, x, a, b):
    # 从最后一步开始跳，倒着推
    # 如果这一步跳a，那么前面的跳法就是n-1步跳到x-a
    # 如果这一步跳b，那么前面的跳法就是n-1步跳到x-b
    # 两种方式只要有一种成功，就可以
    if n == 0:
        return False
    if x == a[n-1] or x == b[n-1]:
        return True
    return jump(n-1, x-a[n-1], a, b) or jump(n-1, x-b[n-1], a, b)
