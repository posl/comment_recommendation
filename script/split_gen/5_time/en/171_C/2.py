def main():
    n = int(input())
    s = ""
    while n > 0:
        n -= 1
        s = chr(n%26 + ord('a')) + s
        n //= 26
    print(s)
