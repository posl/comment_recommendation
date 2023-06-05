def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(0)
    a.reverse()
    a.append(n+1)
    a.reverse()
    ans = 0
    for i in range(k+1):
        ans += (a[i+1]-a[i])*(i+1)
    print(ans)
