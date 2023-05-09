def main():
    N = int(input())
    if N <= 999:
        print(0)
        return
    N = N - 999
    ans = 0
    i = 0
    while N > 0:
        ans += N % 1000
        N = N // 1000
        i += 1
        ans += i * 1
    ans -= 1
    print(ans)
