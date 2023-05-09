def can_pay_exact(x, coins):
    if x == 0:
        return True
    if len(coins) == 0:
        return False
    if x < 0:
        return False
    if x >= coins[0]:
        return can_pay_exact(x - coins[0], coins[1:]) or can_pay_exact(x, coins[1:])
    else:
        return can_pay_exact(x, coins[1:])
    
n, x = map(int, input().split())
coins = []
for i in range(n):
    a, b = map(int, input().split())
    coins.append(a * b)

if __name__ == '__main__':
    can_pay_exact()