def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if p == sum(a[i:j]) and q == sum(a[j:k]) and r == sum(a[k:l]):
                        ans += 1
    if ans > 0:
        print('Yes')
    else:
        print('No')
