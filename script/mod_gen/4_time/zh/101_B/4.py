def S(n):
    result = 0
    while n > 0:
        result += n%10
        n //= 10
    return result
n = int(input())

if __name__ == '__main__':
    S()