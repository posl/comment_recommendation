def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(1,n+1):
        for j in range(k):
            if a[j] <= i:
                ans = max(ans,i-a[j])
            else:
                break
    print(ans)
