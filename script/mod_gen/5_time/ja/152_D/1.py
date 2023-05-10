def calc(n):
    ans = 0
    for i in range(1, n+1):
        s = str(i)
        if s[-1] == s[0]:
            ans += 1
    return ans

if __name__ == '__main__':
    calc()