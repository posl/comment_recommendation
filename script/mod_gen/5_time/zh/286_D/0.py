def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)
    for i in range(1,n):
        a[0] = a[0]*b[i]+a[i]*b[0]
        b[0] = b[0]*b[i]
    if x%a[0] == 0:
        print("Yes")
    else:
        print("No")
main()
