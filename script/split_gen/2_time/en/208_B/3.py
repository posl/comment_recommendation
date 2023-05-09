def main():
    P = int(input())
    coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    factorials = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    coins.reverse()
    factorials.reverse()
    count = 0
    for i in range(len(coins)):
        if P >= factorials[i]:
            count += P // factorials[i]
            P = P % factorials[i]
        if P == 0:
            break
    print(count)
