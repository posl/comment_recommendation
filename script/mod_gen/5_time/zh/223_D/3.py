def f(n,m,a,b):
    ans = []
    for i in range(n):
        ans.append(i+1)
    for i in range(m):
        if ans.index(a[i]) < ans.index(b[i]):
            continue
        else:
            return -1
    return ans

if __name__ == '__main__':
    f()