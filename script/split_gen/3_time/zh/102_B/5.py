def get_max_abs_diff():
    n = int(input())
    a = list(map(int, input().split()))
    min_num = a[0]
    max_num = a[0]
    for i in a:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    return max_num - min_num
