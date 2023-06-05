def main():
    n = int(input())
    name = ''
    while n > 0:
        n -= 1
        name = chr(n%26 + ord('a')) + name
        n //= 26
    print(name)
