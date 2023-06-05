def main():
    n = int(input())
    a = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    ans = 0
    for i in range(n):
        sum -= a[i]
        ans += sum * a[i]
    print(ans % (10**9+7))
