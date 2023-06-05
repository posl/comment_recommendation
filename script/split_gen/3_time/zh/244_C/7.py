def main():
    n = int(input())
    print(1, flush=True)
    a = int(input())
    if a == 0:
        exit()
    l = 2
    r = 2 * n + 1
    while True:
        if l == r:
            print(l, flush=True)
            a = int(input())
            if a == 0:
                exit()
            l = 2
            r = 2 * n + 1
            continue
        m = (l + r) // 2
        print(m, flush=True)
        a = int(input())
        if a == 0:
            exit()
        if (a < m and l <= a) or (m < a and a <= r):
            if a < m:
                r = m - 1
            else:
                l = m + 1
        else:
            if a < m:
                l = m + 1
            else:
                r = m - 1
