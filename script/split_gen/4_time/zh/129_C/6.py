def main():
    n,m = map(int,input().split())
    a = [0] * (n+1)
    for i in range(m):
        a[int(input())] = -1
    a[0] = 1
    for i in range(1,n+1):
        if a[i] != -1:
            if a[i-1] != -1:
                a[i] += a[i-1]
            if a[i-2] != -1:
                a[i] += a[i-2]
            a[i] %= 1000000007
    print(a[n])
