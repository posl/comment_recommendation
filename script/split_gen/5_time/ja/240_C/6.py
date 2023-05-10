def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    # print(n,x,a,b)
    pos = 0
    for i in range(n):
        pos += a[i]
        if pos == x:
            print('Yes')
            return
        pos += b[i]
        if pos == x:
            print('Yes')
            return
    print('No')
