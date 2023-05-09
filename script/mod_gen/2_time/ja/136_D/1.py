def main():
    s = input()
    n = len(s)
    l = [0] * n
    r = [0] * n
    for i in range(n):
        if s[i] == 'L':
            l[i] = 1
        else:
            r[i] = 1
    for i in range(n):
        if i > 0:
            l[i] += l[i-1]
        if i < n-1:
            r[n-1-i] += r[n-i]
    for i in range(n):
        print(l[i] + r[i], end=' ')

if __name__ == '__main__':
    main()