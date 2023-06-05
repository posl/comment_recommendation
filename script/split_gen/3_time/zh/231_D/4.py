def main():
    n,m = map(int,input().split())
    if n == 1:
        print("Yes")
        return
    if m == 0:
        print("No")
        return
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()
    cnt = 0
    for i in range(m-1):
        if b[i] == a[i+1]:
            cnt += 1
    if cnt == m-1:
        print("Yes")
    else:
        print("No")
