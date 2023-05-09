def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n):
        a[i] -= 1
    ans = [0] * n
    for i in range(1, n):
        ans[a[i]] += 1
    for i in range(n):
        print(ans[i])
