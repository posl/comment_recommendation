def main():
    n,q = map(int,input().split())
    t = []
    a = []
    b = []
    for i in range(q):
        t1,a1,b1 = map(int,input().split())
        t.append(t1)
        a.append(a1)
        b.append(b1)
    for i in range(q):
        if t[i] == 1:
            print("No")
        elif t[i] == 2:
            print("No")
        else:
            if a[i] == b[i]:
                print("Yes")
            else:
                print("No")
