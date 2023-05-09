def main():
    n = int(input())
    ans = ""
    while n > 0:
        if n % 2 == 0:
            ans += "B"
            n //= 2
        else:
            ans += "A"
            n -= 1
    print(ans[::-1])
