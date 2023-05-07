def main():
    p = int(input())
    coin = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    ans = 0
    for i in range(9, -1, -1):
        ans += p // coin[i]
        p %= coin[i]
    print(ans)
