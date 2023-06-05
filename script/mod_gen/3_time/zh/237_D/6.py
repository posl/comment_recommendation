def main():
    n = int(input())
    s = input()
    l = 0
    r = n
    ans = [0] * (n+1)
    for i in range(n):
        if s[i] == 'L':
            r -= 1
            ans[r] = i + 1
        else:
            l += 1
            ans[l] = i + 1
    print(' '.join(map(str,ans[l:r])))

if __name__ == '__main__':
    main()