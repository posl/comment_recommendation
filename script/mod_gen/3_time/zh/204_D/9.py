def solve(n, t):
    if n == 1:
        return t[0]
    if n == 2:
        return max(t[0], t[1])
    if n == 3:
        return min(max(t[0], t[1]), t[2])
    if n == 4:
        return min(max(t[0], t[1]) + max(t[2], t[3]), min(max(t[0], t[2]) + max(t[1], t[3]), max(t[0], t[3]) + max(t[1], t[2])))
    if n == 5:
        return min(max(t[0], t[1]) + max(t[2], t[3]) + t[4], min(max(t[0], t[2]) + max(t[1], t[3]) + t[4], max(t[0], t[3]) + max(t[1], t[2]) + t[4], min(max(t[0], t[1]) + t[2] + t[3], max(t[0], t[2]) + t[1] + t[3], max(t[0], t[3]) + t[1] + t[2])))
    if n == 6:
        return min(max(t[0], t[1]) + max(t[2], t[3]) + max(t[4], t[5]), min(max(t[0], t[2]) + max(t[1], t[3]) + max(t[4], t[5]), max(t[0], t[3]) + max(t[1], t[2]) + max(t[4], t[5]), min(max(t[0], t[1]) + max(t[2], t[4]) + t[3], max(t[0], t[1]) + max(t[2], t[5]) + t[3], max(t[0], t[1]) + max(t[3], t[4]) + t[2], max(t[0], t[1]) + max(t[3], t[5]) + t[2], max(t[0], t[1]) + max(t[4], t[5]) + t[2], max(t[0], t[2]) + max(t[

if __name__ == '__main__':
    solve()