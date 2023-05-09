def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for i in range(n):
        ans += (i - n//2) * (x[i] - x[n//2])
    print(ans)
