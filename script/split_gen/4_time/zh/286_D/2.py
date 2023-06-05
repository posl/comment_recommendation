def pay(x, coins, remain):
    if x == 0:
        return True
    if remain == 0:
        return False
    if x < 0:
        return False
    return pay(x, coins, remain - 1) or pay(x - coins[remain - 1], coins, remain - 1)
n, x = map(int, input().split())
coins = []
for i in range(n):
    a, b = map(int, input().split())
    coins.append(a * b)
