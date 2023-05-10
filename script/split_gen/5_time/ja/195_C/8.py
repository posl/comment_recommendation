def main():
    n = int(input())
    if n < 1000:
        print(0)
        return
    ans = 0
    for i in range(1, 16):
        if 1000**i <= n:
            ans += n - 1000**i + 1
    print(ans)
