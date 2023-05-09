def main():
    P = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    ans = 0
    for c in coins[::-1]:
        ans += P // c
        P %= c
    print(ans)
