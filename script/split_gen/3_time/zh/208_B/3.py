def main():
    p = int(input())
    n = 10
    a = [1]
    for i in range(1, n):
        a.append(a[i-1] * (i+1))
    c = 0
    for i in range(n-1, -1, -1):
        c += p // a[i]
        p %= a[i]
    print(c)
