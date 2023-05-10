def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(360)
    a.sort()
    ans = 0
    for i in range(n+1):
        ans = max(ans, (a[i+1]-a[i])%360)
    print(360-ans)
