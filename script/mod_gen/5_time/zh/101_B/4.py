def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
N = int(input())

if __name__ == '__main__':
    S()