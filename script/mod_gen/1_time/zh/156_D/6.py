def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == '__main__':
    gcd()