def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    xy = [list(map(int,input().split())) for i in range(m)]
    now = t
    for i in range(n-1):
        now -= a[i]
        if now <= 0:
            print("No")
            exit()
        for j in range(m):
            if i+1 == xy[j][0]:
                now += xy[j][1]
                break
            elif i+1 < xy[j][0]:
                break
    print("Yes")
