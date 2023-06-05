def get_all_way(h,w,a,b):
    if a == 0 and b == 0:
        return 1
    if a == 0:
        return get_all_way(h,w,a,b-1)
    if b == 0:
        return get_all_way(h,w,a-1,b)
    return get_all_way(h,w,a-1,b)+get_all_way(h,w,a,b-1)
