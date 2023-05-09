def coin(P):
    coins = []
    for i in range(1,11):
        coins.append(i)
    coins.reverse()
    count = 0
    for coin in coins:
        if P == 0:
            break
        if P >= coin:
            count += P // coin
            P = P % coin
    return count
P = int(input())
print(coin(P))

if __name__ == '__main__':
    coin()