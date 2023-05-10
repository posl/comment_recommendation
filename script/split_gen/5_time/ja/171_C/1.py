def solve():
    n = int(input())
    if n <= 26:
        print(chr(n + 96))
        return
    n -= 26
    n -= 1
    c = 1
    while True:
        if n - 26 ** c <= 0:
            break
        n -= 26 ** c
        c += 1
    s = ""
    for i in range(c):
        s += chr(n % 26 + 97)
        n //= 26
    print(s[::-1])
