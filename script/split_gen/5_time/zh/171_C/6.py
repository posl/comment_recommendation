def main():
    n = int(input())
    n -= 1
    base = 26
    length = 1
    while n >= base:
        n -= base
        base *= 26
        length += 1
    ans = ""
    for i in range(length):
        ans = chr(ord("a") + n % 26) + ans
        n //= 26
    print(ans)
