def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = a[i] * 2 - ans[i-1]
    print(*ans)
