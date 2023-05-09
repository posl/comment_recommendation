def swap(p,q,r,s,a):
    b = list(a)
    for i in range(p-1,q):
        b[i] = a[i+r-q]
    for i in range(r-1,s):
        b[i] = a[i+q-p]
    return b
n,p,q,r,s = map(int,input().split())
a = list(map(int,input().split()))
b = swap(p,q,r,s,a)
print(' '.join([str(x) for x in b]))

if __name__ == '__main__':
    swap()