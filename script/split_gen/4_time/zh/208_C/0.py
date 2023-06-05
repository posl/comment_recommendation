def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = k // n
    remain = k % n
    ans = [cnt] * n
    for i in range(remain):
        ans[a[i] - 1] += 1
    for i in range(n):
        print(ans[i])
