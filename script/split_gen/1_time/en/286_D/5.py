def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        aa,bb = map(int,input().split())
        a.append(aa)
        b.append(bb)
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    if sum <= x:
        print("Yes")
    else:
        print("No")
