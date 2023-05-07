def main():
    # put your code here
    n = int(input())
    base = 26
    ans = ''
    while n > 0:
        n -= 1
        ans = chr(n % base + ord('a')) + ans
        n //= base
    print(ans)
