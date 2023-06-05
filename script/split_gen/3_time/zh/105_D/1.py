def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i]%m==0:
            a[i]=0
        else:
            a[i]=a[i]%m
    for i in range(1,n):
        a[i] += a[i-1]
    mod = {}
    for i in range(n):
        if a[i] in mod:
            mod[a[i]] += 1
        else:
            mod[a[i]] = 1
    ans = 0
    for key in mod:
        ans += mod[key]*(mod[key]-1)//2
    ans += mod[0]
    print(ans)
