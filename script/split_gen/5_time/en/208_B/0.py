def main():
    p = int(input())
    coins = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
    count = 0
    for c in coins:
        while p >= c:
            p -= c
            count += 1
    print(count)
