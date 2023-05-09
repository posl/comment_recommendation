def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    for i in range(n):
        ans[i] = k // n
        if i < k % n:
            ans[i] += 1
    for i in range(n):
        if a[i] <= k:
            ans[i] += k // n
            if i < k % n:
                ans[i] += 1
        else:
            break
    for i in range(n):
        print(ans[i])
