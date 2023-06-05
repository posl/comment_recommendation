def main():
    n = int(input())
    s = input()
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'L':
            l += 1
        else:
            r += 1
    print(' '.join(map(str, list(range(l+1, 1, -1)) + list(range(l+2, n+1)))))

if __name__ == '__main__':
    main()