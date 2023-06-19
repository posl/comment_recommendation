def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            ans = max(ans, sum)
    print(ans)
