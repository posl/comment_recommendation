def get_max_count(h,w):
    if h == 1 and w == 1:
        return 1
    elif h == 1:
        return w-1
    elif w == 1:
        return h-1
    else:
        return h*w-1

if __name__ == '__main__':
    get_max_count()