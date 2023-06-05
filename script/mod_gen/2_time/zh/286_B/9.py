def swap(p,q,r,s):
    for i in range(p-1,q):
        temp = a[i]
        a[i] = a[s-1]
        a[s-1] = temp
        s = s-1
    for i in range(r-1,s):
        temp = a[i]
        a[i] = a[q-1]
        a[q-1] = temp
        q = q+1
    return a
n,p,q,r,s = map(int,input().split())
a = list(map(int,input().split()))
b = swap(p,q,r,s)
print(*b)

if __name__ == '__main__':
    swap()