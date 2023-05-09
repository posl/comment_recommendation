def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = a[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b + i + 1))
    print(ans)
