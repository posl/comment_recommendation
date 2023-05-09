def main():
    n = int(input())
    a = 26
    b = 0
    while n > a:
        n -= a
        b += 1
        a *= 26
    l = []
    for i in range(b):
        l.append(n % 26)
        n //= 26
    l.append(n)
    l.reverse()
    for i in l:
        print(chr(i+96), end="")
    print()
