def get_max(a,b,c,d):
    x = [a,b]
    y = [c,d]
    max_x = max(x)
    min_x = min(x)
    max_y = max(y)
    min_y = min(y)
    if max_x * max_y >= max_x * min_y:
        if max_x * max_y >= min_x * max_y:
            if max_x * max_y >= min_x * min_y:
                return max_x * max_y
            else:
                return min_x * min_y
        else:
            if min_x * max_y >= min_x * min_y:
                return min_x * max_y
            else:
                return min_x * min_y
    else:
        if min_x * max_y >= min_x * min_y:
            if min_x * max_y >= max_x * min_y:
                return min_x * max_y
            else:
                return max_x * min_y
        else:
            if min_x * min_y >= max_x * min_y:
                return min_x * min_y
            else:
                return max_x * min_y

if __name__ == '__main__':
    get_max()