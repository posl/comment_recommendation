def main():
    P = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    count = 0
    for i in range(9, -1, -1):
        if P >= coins[i]:
            count += P // coins[i]
            P = P % coins[i]
    print(count)
