def isSquare(n):
    if n < 0:
        return False
    x = int(n ** 0.5)
    return x * x == n

if __name__ == '__main__':
    isSquare()