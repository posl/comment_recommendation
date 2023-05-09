def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        if k & (1 << i):
            cnt = 0
            for j in range(n):
                if a[j] & (1 << i):
                    cnt += 1
            if cnt * 2 < n:
                ans += 1 << i
            k -= 1 << i
    print(ans)
