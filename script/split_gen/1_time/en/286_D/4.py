def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    ans = 0
    for i in range(n):
        ans = ans + a[i]*b[i]
    if ans <= x:
        print("Yes")
    else:
        print("No")
