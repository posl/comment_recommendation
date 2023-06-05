def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        ans = max(ans, sum)
    print(ans)
