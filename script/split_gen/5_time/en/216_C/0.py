def main():
    n = int(input())
    s = ''
    while n > 0:
        if n % 2 == 1:
            s = 'A' + s
            n -= 1
        else:
            s = 'B' + s
            n //= 2
    print(s)
