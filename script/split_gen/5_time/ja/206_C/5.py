def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (n-i-1)
    for i in range(1,n):
        if a[i-1] == a[i]:
            ans -= 1
    print(ans)
