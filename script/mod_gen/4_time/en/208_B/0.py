def main():
    p = int(input())
    coins = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
    count = 0
    for i in coins:
        while p >= i:
            p -= i
            count += 1
    print(count)

if __name__ == '__main__':
    main()