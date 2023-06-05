def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    # print(a,b)
    # a.sort()
    # b.sort()
    # print(a,b)
    # print(a[0],b[0])
    # print(a[0]-0.5)
    # print(b[-1]+0.5)
    if a[0]-0.5 > 0:
        print("No")
        return
    if b[-1]+0.5 < t:
        print("No")
        return
    for i in range(m-1):
        if b[i]+0.5 < a[i+1]-0.5:
            print("No")
            return
    print("Yes")
