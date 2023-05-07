def main():
    p = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    coins.reverse()
    cnt = 0
    for c in coins:
        cnt += p // c
        p %= c
    print(cnt)
