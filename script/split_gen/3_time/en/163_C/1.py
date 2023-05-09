def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n - 1):
        ans[a[i] - 1] += 1
    for i in range(n):
        print(ans[i])
