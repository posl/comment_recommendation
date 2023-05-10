def main():
    s = input()
    n = len(s)
    a = [0]*n
    l, r = 0, 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        else:
            l += 1
            a[i] += l//2
            a[i-1] += (l+1)//2
            l = 0
    l, r = 0, 0
    for i in range(n-1, -1, -1):
        if s[i] == 'L':
            l += 1
        else:
            r += 1
            a[i] += r//2
            a[i+1] += (r+1)//2
            r = 0
    print(*a)
main()
