def climb_stairs(n, m, a):
    if m == 0:
        return 1
    a.append(n)
    a.insert(0, 0)
    result = 1
    for i in range(1, m + 2):
        result *= (a[i] - a[i - 1])
    return result % 1000000007

if __name__ == '__main__':
    climb_stairs()