def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(n)
    ans = 0
    for i in range(k):
        ans += (a[i+1]-a[i])*(i+1)
    print(ans)
