def f(s):
    ans = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if int(s[i:j]) % 2019 == 0:
                ans += 1
    return ans

if __name__ == '__main__':
    f()