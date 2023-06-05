def is_sum_possible(a, b, s):
    if s == 0:
        return True
    if len(a) == 0:
        return False
    return is_sum_possible(a[1:], b[1:], s) or is_sum_possible(a[1:], b[1:], s-a[0]-b[0]) or is_sum_possible(a[1:], b[1:], s-a[0]) or is_sum_possible(a[1:], b[1:], s-b[0])

if __name__ == '__main__':
    is_sum_possible()