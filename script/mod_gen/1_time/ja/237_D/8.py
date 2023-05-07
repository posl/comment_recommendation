def main():
    import sys
    readline = sys.stdin.readline
    n = int(readline())
    s = readline().rstrip()
    ans = []
    l = 0
    r = n
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            ans.append(r)
            r -= 1
        else:
            ans.append(l)
            l += 1
    print(*ans[::-1])

if __name__ == '__main__':
    main()