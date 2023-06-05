def f(n,x,s):
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans = ans // 2
        elif s[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    return ans

if __name__ == '__main__':
    f()