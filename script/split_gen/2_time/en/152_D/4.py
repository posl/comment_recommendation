def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += 9 * (i // 10) + (i % 10)
    print(ans)
