def get_max_sum(a, m):
    if m == 0:
        return 0
    if m == 1:
        return max(a)
    if m == 2:
        return max(a[0] + 2 * a[1], 2 * a[0] + a[1])
    if m == 3:
        return max(a[0] + 2 * a[1] + 3 * a[2], a[0] + 2 * a[1] + a[2] + a[3], 2 * a[0] + a[1] + a[2] + a[3])
    if m == 4:
        return max(a[0] + 2 * a[1] + 3 * a[2] + 4 * a[3], a[0] + 2 * a[1] + 3 * a[2] + a[3] + a[4], a[0] + 2 * a[1] + a[2] + a[3] + a[4] + a[5], 2 * a[0] + a[1] + a[2] + a[3] + a[4] + a[5])
    if m == 5:
        return max(a[0] + 2 * a[1] + 3 * a[2] + 4 * a[3] + 5 * a[4], a[0] + 2 * a[1] + 3 * a[2] + 4 * a[3] + a[4] + a[5], a[0] + 2 * a[1] + 3 * a[2] + a[3] + a[4] + a[5] + a[6], a[0] + 2 * a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7], 2 * a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7])
    if m == 6:
        return max(a[0] + 2 * a[1

if __name__ == '__main__':
    get_max_sum()