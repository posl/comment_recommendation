def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(n):
        x = i + 1
        cnt = 0
        while x < k:
            x *= 2
            cnt += 1
        ans += (1 / (2 ** cnt)) / n
    print(ans)
