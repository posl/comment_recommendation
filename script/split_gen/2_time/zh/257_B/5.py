def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    for i in range(q):
        for j in range(k):
            if l[j] == n:
                continue
            if a[l[j]-1] == a[l[j]]:
                continue
            if a[l[j]] == a[l[j]-1]+1:
                a[l[j]-1],a[l[j]] = a[l[j]],a[l[j]-1]
    print(*a)
