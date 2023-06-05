def main():
    n,w = map(int, input().split())
    a = []
    for i in range(n):
        s,t,p = map(int, input().split())
        a.append((s,p))
        a.append((t,-p))
    a.sort()
    for i in range(1,2*n):
        a[i] = (a[i-1][1]+a[i][1],a[i][0])
    for i in range(2*n):
        if a[i][0] > w:
            print("No")
            return
    print("Yes")
