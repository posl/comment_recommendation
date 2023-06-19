def main():
    n,m = map(int,input().split())
    city = [0]*n
    for i in range(m):
        a,b = map(int,input().split())
        city[a-1] += 1
        city[b-1] += 1
    ans = 0
    for i in range(n):
        ans += city[i]*(n-1-city[i])
    print(ans//2)
