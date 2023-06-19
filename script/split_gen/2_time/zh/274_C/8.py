def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(1, 2 * n):
        print(ans[i])
