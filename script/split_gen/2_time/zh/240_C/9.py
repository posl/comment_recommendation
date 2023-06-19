def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ta,tb = map(int,input().split())
        a.append(ta)
        b.append(tb)
    pos = 0
    for i in range(n):
        if (pos + a[i]) > x:
            print("No")
            return
        else:
            pos += b[i] - a[i]
    if pos == x:
        print("Yes")
    else:
        print("No")
