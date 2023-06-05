def find_max_num(n, m, a):
    a.sort(reverse=True)
    i = 0
    while i < m:
        if n >= a[i]:
            n = n - a[i]
            print(a[i], end='')
            i = 0
        else:
            i += 1

if __name__ == '__main__':
    find_max_num()