def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            n //= 2
            s += "B"
        else:
            n -= 1
            s += "A"
    print(s[::-1])
