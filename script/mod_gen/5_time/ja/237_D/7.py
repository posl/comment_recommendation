def main():
    n = int(input())
    s = input()
    ans = []
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'L':
            l = l + 1
            ans.append(l)
        else:
            r = r + 1
            ans.insert(0, r)
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()