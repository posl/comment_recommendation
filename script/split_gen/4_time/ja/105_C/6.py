def main():
    n = int(input())
    if n == 0:
        print(0)
        exit()
    ans = ""
    while n != 0:
        if n % 2 != 0:
            ans = "1" + ans
            n -= 1
        else:
            ans = "0" + ans
        n //= -2
    print(ans)
