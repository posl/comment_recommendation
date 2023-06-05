def main():
    s = input()
    n = len(s)
    ans = [0]*n
    l = 0
    r = 0
    for i in range(n):
        if s[i] == "L":
            l = i
        if s[i] == "R":
            r = i
    for i in range(n):
        if s[i] == "R":
            if (r-i)%2 == 0:
                ans[r] += 1
            else:
                ans[r+1] += 1
        if s[i] == "L":
            if (i-l)%2 == 0:
                ans[l] += 1
            else:
                ans[l-1] += 1
    print(*ans)

if __name__ == '__main__':
    main()