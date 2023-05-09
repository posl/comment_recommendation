def main():
    P = int(input())
    coins = [1]
    i = 1
    while i <= 9:
        coins.append(coins[i-1] * (i+1))
        i += 1
    i = 9
    count = 0
    while P > 0:
        if P >= coins[i]:
            P -= coins[i]
            count += 1
        else:
            i -= 1
    print(count)

if __name__ == '__main__':
    main()