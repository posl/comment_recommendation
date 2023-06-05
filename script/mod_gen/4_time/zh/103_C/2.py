def f(m, a):
    ans = 0
    for i in range(len(a)):
        ans += m % a[i]
    return ans

if __name__ == '__main__':
    f()