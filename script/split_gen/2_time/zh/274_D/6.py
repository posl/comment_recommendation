def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(1, n + 1):
        p = i
        cnt = 0
        while True:
            cnt += 1
            p = a[p]
            if p == 1:
                break
        ans[i] = cnt
    for i in range(1, 2 * n + 1):
        print(ans[i])
