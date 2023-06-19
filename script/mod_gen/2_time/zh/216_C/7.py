def main():
    n = int(input())
    ans = ""
    while n > 0:
        if n % 2 == 0:
            n //= 2
            ans = "B" + ans
        else:
            n -= 1
            ans = "A" + ans
    print(ans)

if __name__ == '__main__':
    main()