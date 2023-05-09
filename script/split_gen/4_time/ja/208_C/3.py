def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0] * n
    cnt = k // n
    k %= n
    for i in range(n):
        ans[i] = cnt
    b = sorted(a)
    for i in range(k):
        ans[b[i] - 1] += 1
    for i in range(n):
        print(ans[i])
