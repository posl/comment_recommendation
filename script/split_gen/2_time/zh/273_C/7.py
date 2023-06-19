def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = [0] * n
    ans[0] = 1
    cnt = 1
    for i in range(1, n):
        if a[i] != a[i-1]:
            cnt += 1
        ans[i] = cnt
    for i in range(n):
        print(ans[i])
