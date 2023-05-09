def main():
    N, A, B = map(int, input().split())
    ans = 0
    ans += (N // A) * (A * (A + 1) // 2)
    ans += (N // B) * (B * (B + 1) // 2)
    ans -= (N // (A * B)) * (A * B * (A * B + 1) // 2)
    ans -= (N // A) * (N // A + 1) // 2 * A
    ans -= (N // B) * (N // B + 1) // 2 * B
    ans += (N // (A * B)) * (N // (A * B) + 1) // 2 * A * B
    print(ans)
