def main():
    n,p,q,r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if p == sum(a[i:j+1]) and q == sum(a[j:k+1]) and r == sum(a[k:l+1]):
                        ans += 1
    if ans > 0:
        print('Yes')
    else:
        print('No')
