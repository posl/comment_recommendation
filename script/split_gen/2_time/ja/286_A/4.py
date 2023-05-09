def main():
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        if p <= i+1 <= q:
            b.append(a[r-1+i-q])
        elif r <= i+1 <= s:
            b.append(a[p-1+i-r])
        else:
            b.append(a[i])
    print(*b)
