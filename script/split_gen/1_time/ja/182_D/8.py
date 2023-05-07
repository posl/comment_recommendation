def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    max_val = 0
    for i in range(n):
        ans += a[i]
        max_val = max(max_val, ans)
    print(max_val)
