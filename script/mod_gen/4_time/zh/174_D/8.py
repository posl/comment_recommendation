def main():
    n = int(input())
    c = input()
    l = 0
    r = n-1
    ans = 0
    while l < r:
        if c[l] == 'W':
            if c[r] == 'R':
                ans += 1
                l += 1
                r -= 1
            else:
                r -= 1
        else:
            l += 1
    print(ans)

if __name__ == '__main__':
    main()