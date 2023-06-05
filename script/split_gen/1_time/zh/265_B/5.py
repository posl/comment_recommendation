def main():
    n,m,t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = []
    for _ in range(m):
        xy.append(list(map(int, input().split())))
    for i in range(m):
        a[xy[i][0]-2] += xy[i][1]
    for i in range(n-1):
        t -= a[i]
        if t <= 0:
            print("No")
            return
    print("Yes")
