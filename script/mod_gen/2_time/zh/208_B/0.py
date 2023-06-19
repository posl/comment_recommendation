def get_coins(p):
    coins = [1,2,6,24,120,720,5040,40320,362880,3628800]
    count = 0
    for i in range(9,-1,-1):
        while p >= coins[i]:
            p -= coins[i]
            count += 1
    return count

if __name__ == '__main__':
    get_coins()