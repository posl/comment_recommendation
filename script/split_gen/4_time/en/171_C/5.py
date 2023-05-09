def main():
    import sys
    import math
    n = int(input())
    ans = ''
    while n > 0:
        n -= 1
        ans += chr(n % 26 + ord('a'))
        n //= 26
    print(ans[::-1])
