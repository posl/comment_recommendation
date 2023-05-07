def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n-1):
        if a[i] <= a[i+1]:
            ans += a[i+1] - a[i] + 1
            a[i+1] = a[i] - 1
    print(ans)
