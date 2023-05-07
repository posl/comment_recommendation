def main():
    n = int(input())
    name = ''
    while n > 0:
        n -= 1
        name = chr(ord('a') + n % 26) + name
        n //= 26
    print(name)
