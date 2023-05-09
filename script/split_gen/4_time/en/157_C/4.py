def main():
    n, m = map(int, input().split())
    s = []
    c = []
    for i in range(m):
        a, b = map(int, input().split())
        s.append(a)
        c.append(b)
    for i in range(10**(n-1), 10**n):
        ii = str(i)
        flag = True
        for j in range(m):
            if ii[s[j]-1] != str(c[j]):
                flag = False
        if flag:
            print(i)
            return
    print(-1)
