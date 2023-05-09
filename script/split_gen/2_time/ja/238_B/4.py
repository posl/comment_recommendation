def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i%360 for i in a]
    a.sort()
    a.append(a[0]+360)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i+1]-a[i])
    print(360-ans)
