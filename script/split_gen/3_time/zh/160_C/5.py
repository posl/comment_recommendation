def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(k+a[0])
    ans = k
    for i in range(n):
        ans = min(ans,a[i+1]-a[i])
    print(ans)
