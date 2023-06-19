def main():
    n,m,t = map(int,input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(m):
        if i==0:
            if a[i]>1:
                print('No')
                return
        else:
            if a[i]-b[i-1]>2:
                print('No')
                return
    if t-b[m-1]>2:
        print('No')
        return
    print('Yes')
