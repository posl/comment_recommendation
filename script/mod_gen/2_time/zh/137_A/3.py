def main():
    s = input()
    n = len(s)
    ans = [0]*n
    for i in range(n):
        if s[i] == 'R':
            ans[i+1] += 1
        else:
            ans[i] += 1
    for i in range(10**100):
        for j in range(n):
            if s[j] == 'R':
                ans[j+1] += 1
            else:
                ans[j] += 1
    print(*ans)

if __name__ == '__main__':
    main()