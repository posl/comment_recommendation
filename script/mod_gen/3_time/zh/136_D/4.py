def main():
    s = input()
    n = len(s)
    r = [0] * n
    l = [0] * n
    r_count = 0
    l_count = 0
    for i in range(n):
        if s[i] == 'R':
            r_count += 1
        else:
            r_count = 0
        r[i] = r_count
    for i in range(n-1, -1, -1):
        if s[i] == 'L':
            l_count += 1
        else:
            l_count = 0
        l[i] = l_count
    for i in range(n):
        if s[i] == 'R' and s[i+1] == 'L':
            r[i] += 1
            l[i+1] += 1
    for i in range(n):
        print(r[i]+l[i], end=' ')
    print()

if __name__ == '__main__':
    main()