def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    ans[0] = n - 1
    cnt = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            cnt += 1
        else:
            cnt = 1
        ans[i] = n - i - 1 - cnt
    for i in range(n):
        print(ans[i])
