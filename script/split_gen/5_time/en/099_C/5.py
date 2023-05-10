def main():
    N = int(input())
    ans = N
    for i in range(1, N+1):
        cnt = 0
        x = i
        while x > 0:
            cnt += x % 6
            x //= 6
        x = N - i
        while x > 0:
            cnt += x % 9
            x //= 9
        ans = min(ans, cnt)
    print(ans)
