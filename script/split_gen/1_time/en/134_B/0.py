def main():
    N, D = map(int, input().split())
    ans = N // (2 * D + 1)
    if N % (2 * D + 1) != 0:
        ans += 1
    print(ans)
