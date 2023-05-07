def main():
    s = input()
    n = len(s)
    l = [1] * n
    for i in range(n):
        if s[i] == 'L':
            l[i-1] += l[i]
            l[i] = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'R':
            l[i+1] += l[i]
            l[i] = 0
    print(*l)

if __name__ == '__main__':
    main()