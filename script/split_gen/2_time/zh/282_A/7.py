def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    ans = -1
    for i in range(1,n+1):
        for j in range(i,n+1):
            if j-i+1 == k:
                if sum(a[i-1:j]) % d != 0:
                    ans = max(ans,sum(a[i-1:j]))
    print(ans)
