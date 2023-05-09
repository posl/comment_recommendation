def main():
    n,m,t = map(int,input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    #print(a,b)
    now = n
    for i in range(m):
        now -= a[i] - b[i - 1]
        if now <= 0:
            print("No")
            return
        now += b[i] - a[i]
        if now > n:
            now = n
    now -= t - b[m - 1]
    if now <= 0:
        print("No")
        return
    print("Yes")
