def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            ans += n-i-1
    print(ans)
