def main():
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0]*n
    for i in range(k):
        b[a[i]-1] = i+1
    for i in range(q):
        if b[l[i]-1] != 0:
            b[l[i]-1],b[l[i]] = b[l[i]],b[l[i]-1]
    for i in range(n):
        print(b[i],end=' ')
