def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0: # 偶数はあらかじめ除外
        return False
    for i in range(3, int(n**0.5)+1, 2): # 3からnの平方根までの奇数で割り切れるかチェック
        if n % i == 0:
            return False
    return True
x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1

if __name__ == '__main__':
    is_prime()