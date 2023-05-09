def main():
    N, A, B = map(int, input().split())
    q, mod = divmod(N, A + B)
    ans = q * A
    ans += min(mod, A)
    print(ans)
