def main():
    n = int(input())
    s = ''
    while n > 0:
        if n % 2 == 0:
            s += 'B'
            n //= 2
        else:
            s += 'A'
            n -= 1
    print(s[::-1])
