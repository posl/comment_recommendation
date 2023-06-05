def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): # int(n**0.5)+1 为了减少循环次数
        if n % i == 0:
            return False
    return True
a, b, c, d = map(int, input().split())

if __name__ == '__main__':
    is_prime()