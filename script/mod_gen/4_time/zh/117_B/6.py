def can_draw_poly(n, l):
    max_len = max(l)
    if max_len < sum(l) - max_len:
        return True
    else:
        return False

if __name__ == '__main__':
    can_draw_poly()