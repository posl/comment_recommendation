def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += bisect.bisect_left(a, a[i] + a[j]) - j - 1
    print(ans)
