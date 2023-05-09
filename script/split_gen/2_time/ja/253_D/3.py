def main():
    N, A, B = map(int, input().split())
    ans = 0
    ans += N // A * (A + 1) * A // 2
    ans += N // B * (B + 1) * B // 2
    ans -= N // (A * B) * (A * B + 1) * (A * B) // 2
    print(ans)
