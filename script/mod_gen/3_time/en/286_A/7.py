def myCode():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if i+1 == p or i+1 == q or i+1 == r or i+1 == s:
            print(a[r-1], end=' ')
        elif i+1 == r or i+1 == s:
            print(a[p-1], end=' ')
        else:
            print(a[i], end=' ')

if __name__ == '__main__':
    myCode()