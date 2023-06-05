def coin(p):
    coin = [1,2,6,24,120,720,5040,40320,362880,3628800]
    count = 0
    for i in range(9,-1,-1):
        count += p // coin[i]
        p = p % coin[i]
    return count
p = int(input())
print(coin(p))
