def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    ans = [0] * (2 ** n + 1)
    for i in range(n):
        ans[a[i]] = ans[a[i] // 2] + 1
    for i in range(2 ** n + 1):
        print(ans[i])
