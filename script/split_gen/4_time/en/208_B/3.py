def main():
    P = int(input())
    coin = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
    ans = 0
    for i in coin:
        ans += P // i
        P %= i
    print(ans)
